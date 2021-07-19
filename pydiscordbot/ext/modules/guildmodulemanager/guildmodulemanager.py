from discord.ext import commands
from asyncio.exceptions import CancelledError, TimeoutError
from dislash import SelectMenu, SelectOption

from ext.modules import Module
from ext.config import settings
from ext.db import models
from ext.utils import checkers


class GuildModuleManager(Module):

    # Auxiliary methods
    def _get_unloaded_modules(self, guild_id):
        try:
            # guild_id = message.guild.id
            unloaded_modules = self.session.query(models.GuildModule).filter(
                models.GuildModule.id == guild_id,
                models.GuildModule.active == False
            ).all()
            return unloaded_modules
        except:
            raise NotImplemented

    def _get_loaded_modules(self, guild_id):
        try:
            # guild_id = message.guild.id
            loaded_modules = self.session.query(models.GuildModule).filter(
                models.GuildModule.id == guild_id,
                models.GuildModule.active == True
            ).all()
            return loaded_modules
        except:
            raise NotImplemented

    # Command methods

    # @commands.command()
    # @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    # async def load_modules(self, ctx):
    #     try:
    #         # set select/dropdown options
    #         select_options = [
    #             SelectOption(label="Cancel", value="cancel", emoji="❌")
    #         ]
    #         for module in self._get_unloaded_modules():
    #             select_options.insert(
    #                 0,
    #                 SelectOption(
    #                     label=module.name.title(),
    #                     value=module.path,
    #                     emoji=module.emoji
    #                 )
    #             )
    #         msg = await ctx.send(
    #             "Select the module to be loaded into the bot:",
    #             components=[
    #                 SelectMenu(
    #                     custom_id="load_module",
    #                     placeholder=f"Choose up to {len(select_options)} modules",
    #                     max_values=len(select_options),
    #                     options=select_options
    #                 )
    #             ]
    #         )
    #         # Wait for a click on the menu that was sent.
    #         inter = await msg.wait_for_dropdown(
    #             check=(lambda m: m.author == ctx.author),
    #             timeout=60
    #         )
    #         # Tells which option was selected. 
    #         selected_options = inter.select_menu.selected_options
    #         selected_labels = [option.label for option in selected_options]
    #         selected_values = [option.value for option in selected_options]
    #         if "cancel" in selected_values:
    #             raise CancelledError()
    #         # Load the modules
    #         for module_path in selected_values:
    #             self.app.load_extension(module_path)
    #         await inter.reply(f"👌 The following module(s) have been loaded: {', '.join(selected_labels)}")
    #     except CancelledError:
    #         await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
    #     except TimeoutError:
    #         await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
    #     except ModuleNotFoundError:
    #         await inter.reply(f"😿 Unknown error. Please contact the administrator. ")

    # @commands.command()
    # @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    # async def unload_modules(self, ctx):
    #     try:
    #         # set select/dropdown options
    #         select_options = [
    #             SelectOption(label="Cancel", value="cancel", emoji="❌")
    #         ]
    #         for module in self._get_loaded_modules():
    #             select_options.insert(
    #                 0,
    #                 SelectOption(
    #                     label=module.name.title(),
    #                     value=module.path,
    #                     emoji=module.emoji
    #                 )
    #             )
    #         msg = await ctx.send(
    #             "Select the module to be unloaded from the bot:",
    #             components=[
    #                 SelectMenu(
    #                     custom_id="unload_module",
    #                     placeholder=f"Choose up to {len(select_options)} modules",
    #                     max_values=len(select_options),
    #                     options=select_options
    #                 )
    #             ]
    #         )
    #         # Wait for a click on the menu that was sent.
    #         inter = await msg.wait_for_dropdown(
    #             check= (lambda m: m.author == ctx.author),
    #             timeout=60
    #         )
    #         # Tells which option was selected. 
    #         selected_options = inter.select_menu.selected_options
    #         selected_labels = [option.label for option in selected_options]
    #         selected_values = [option.value for option in selected_options]
    #         if "cancel" in selected_values:
    #             raise CancelledError()
    #         # Load the modules
    #         for module_path in selected_values:
    #             self.app.unload_extension(module_path)
    #         await inter.reply(f"👌 The following module(s) have been unloaded: {', '.join(selected_labels)}")
    #     except CancelledError:
    #         await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
    #     except TimeoutError:
    #         await msg.reply("⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
    #     except ModuleNotFoundError:
    #         await inter.reply(f"😿 Unknown error. Please contact the administrator. ")


    # @commands.command()
    # @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    # async def reload_modules(self, ctx):
    #     try:
    #         # set select/dropdown options
    #         select_options = [
    #             SelectOption(label="Cancel", value="cancel", emoji="❌")
    #         ]
    #         for module in self._get_loaded_modules():
    #             select_options.insert(
    #                 0,
    #                 SelectOption(
    #                     label=module.name.title(),
    #                     value=module.path,
    #                     emoji=module.emoji
    #                 )
    #             )
    #         msg = await ctx.send(
    #             "Select the module to be reloaded from the bot:",
    #             components=[
    #                 SelectMenu(
    #                     custom_id="reload_module",
    #                     placeholder=f"Choose up to {len(select_options)} modules",
    #                     max_values=len(select_options),
    #                     options=select_options
    #                 )
    #             ]
    #         )
    #         # Wait for a click on the menu that was sent.
    #         inter = await msg.wait_for_dropdown(
    #             check= (lambda m: m.author == ctx.author),
    #             timeout=60
    #         )
    #         # Tells which option was selected. 
    #         selected_options = inter.select_menu.selected_options
    #         selected_labels = [option.label for option in selected_options]
    #         selected_values = [option.value for option in selected_options]
    #         if "cancel" in selected_values:
    #             raise CancelledError()
    #         # Load the modules
    #         for module_path in selected_values:
    #             self.app.unload_extension(module_path)
    #         await inter.reply(f"👌 The following module(s) have been reloaded: {', '.join(selected_labels)}")  
    #     except CancelledError:
    #         await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
    #     except TimeoutError:
    #         await msg.reply("⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
    #     except ModuleNotFoundError:
    #         await inter.reply(f"😿 Unknown error. Please contact the administrator. ")

    # @reload_modules.error
    # @unload_modules.error
    # @load_modules.error
    # async def extension_errors(self, ctx, error):
    #     try:
    #         error_msgs = {
    #             commands.ExtensionNotFound: f"This extension was not found.\nCheck the available modules using the "
    #                                         f"{settings.COMMAND_PREFIX}available_modules command.",
    #             commands.ExtensionAlreadyLoaded: f"This extension already loaded!",
    #             commands.NoEntryPointError: f"This extension can't be loaded! Please contact the system admin.",
    #             commands.ExtensionFailed: f"This extension cannot be loaded because an error was found in it."
    #                                       f"Please contact the system admin.",
    #             commands.ExtensionNotLoaded: f"This extension isn't loaded! You can check loaded extensions"
    #                                          f" using {settings.COMMAND_PREFIX}loaded_extensions"
    #         }
    #         if message := error_msgs.get(type(error.original)):
    #             await ctx.send(message)
    #     except AttributeError:
    #         pass

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.errors.MissingRole):
    #         await ctx.send("You don't have the correct role for this command.")