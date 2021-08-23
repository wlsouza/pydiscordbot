from discord.ext import commands
from dislash import SelectMenu, SelectOption
from asyncio.exceptions import CancelledError, TimeoutError
from sqlalchemy.orm.exc import NoResultFound

from ext.modules import Module
from ext.db import models
from ext.utils import checkers


class GuildModuleManager(Module):

    # Auxiliary methods
    def _get_disabled_modules_of_guild(self, ctx):
        guild_id = ctx.guild.id
        disabled_modules = (
            self.session.query(models.Module)
            .join(models.GuildModule)
            .filter(
                models.GuildModule.guild_id == guild_id,
                models.GuildModule.enabled == False
            ).all()
        )
        return disabled_modules

    def _get_enabled_modules_of_guild(self, ctx):
        guild_id = ctx.guild.id
        enabled_modules = (
            self.session.query(models.Module)
            .join(models.GuildModule)
            .filter(
                models.GuildModule.guild_id == guild_id,
                models.GuildModule.enabled == True
            ).all()
        )
        return enabled_modules

    def _update_guildmodules_of_guild(self, ctx):
        guild_id = ctx.guild.id
        # Get a list of all guildmodules ids from that guild into db
        guild_modules_ids = [
            row.module_id for row in self.session.query(
                models.GuildModule.module_id
            ).filter(
                models.GuildModule.guild_id == guild_id
            )
        ]
        # Get a list of **rows** of disableable modules ids from db
        disableable_module_ids = self.session.query(models.Module.id).filter(
            models.Module.disableable == True
        )
        # For each disableable module id from db check if exists a guildmodule of 
        # that module and guild id and insert it if not
        for module_id, in disableable_module_ids:
            if module_id not in guild_modules_ids:
                guild_module =  models.GuildModule(
                    guild_id = guild_id,
                    module_id = module_id,
                    enabled = False
                )
                self.session.add(guild_module)
                self.session.commit()

    # @commands.command()
    # async def test(self, ctx):
    #     self._update_guildmodules_of_guild(ctx)
    #     self._get_loaded_modules_of_guild(ctx)


    # Command methods
    @commands.command()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    async def enable_modules(self, ctx):
        try:
            self._update_guildmodules_of_guild(ctx)
            # set select/dropdown options
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module in self._get_disabled_modules_of_guild(ctx):
                select_options.insert(
                    0,
                    SelectOption(
                        label=module.name,
                        value=module.id,
                        emoji=module.emoji
                    )
                )
            msg = await ctx.send(
                "Select the module(s) to be enable:",
                components=[
                    SelectMenu(
                        custom_id="enable_guild_module",
                        placeholder=f"Choose up to {len(select_options)} modules",
                        max_values=len(select_options),
                        options=select_options
                    )
                ]
            )
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(
                check=(lambda m: m.author == ctx.author),
                timeout=60
            )
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                raise CancelledError()
            # Set guildmodules.enabled to True
            for module_id in selected_values:
                guild_module = (
                    self.session.query(models.GuildModule)
                    .filter(
                        models.GuildModule.guild_id == ctx.guild.id,
                        models.GuildModule.module_id == module_id
                    ).one()
                )
                guild_module.enabled = True
            self.session.commit()
            await inter.reply(f"👌 The following module(s) has been enabled: {', '.join(selected_labels)}")
        except CancelledError:
            await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
        except NoResultFound:
            await msg.reply(f"😿 The modules could not be enabled, please contact your system administrator.")

    @commands.command()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    async def disable_modules(self, ctx):
        try:
            self._update_guildmodules_of_guild(ctx)
            # set select/dropdown options
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module in self._get_enabled_modules_of_guild(ctx):
                select_options.insert(
                    0,
                    SelectOption(
                        label=module.name,
                        value=module.id,
                        emoji=module.emoji
                    )
                )
            msg = await ctx.send(
                "Select the module(s) to be disable:",
                components=[
                    SelectMenu(
                        custom_id="disable_guild_module",
                        placeholder=f"Choose up to {len(select_options)} modules",
                        max_values=len(select_options),
                        options=select_options
                    )
                ]
            )
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(
                check=(lambda m: m.author == ctx.author),
                timeout=60
            )
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                raise CancelledError()
            # Set guildmodules.enabled to False
            for module_id in selected_values:
                guild_module = (
                    self.session.query(models.GuildModule)
                    .filter(
                        models.GuildModule.guild_id == ctx.guild.id,
                        models.GuildModule.module_id == module_id
                    ).one()
                )
                guild_module.enabled = False
            self.session.commit()
            await inter.reply(f"👌 The following module(s) has been disabled: {', '.join(selected_labels)}")
        except CancelledError:
            await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
        except NoResultFound:
            await msg.reply(f"😿 The modules could not be disabled, please contact your system administrator.")

    @disable_modules.error
    @enable_modules.error
    async def modules_errors(self, ctx, error):
        try:
            error_msgs = {
                commands.ExtensionNotFound: f"This extension was not found.\nPlease contact the system admin.",
                commands.ExtensionAlreadyLoaded: f"This extension already loaded!",
                commands.NoEntryPointError: f"This extension can't be loaded! Please contact the system admin.",
                commands.ExtensionFailed: f"This extension cannot be loaded because an error was found in it."
                                          f"Please contact the system admin.",
                commands.ExtensionNotLoaded: f"This extension isn't loaded!"
            }
            if message := error_msgs.get(type(error.original)):
                await ctx.send(message)
        except AttributeError:
            pass

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.errors.MissingRole):
    #         await ctx.send("You don't have the correct role for this command.")