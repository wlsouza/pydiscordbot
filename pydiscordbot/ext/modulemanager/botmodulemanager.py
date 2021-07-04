from discord.ext import commands
from asyncio.exceptions import TimeoutError
from dislash import SelectMenu, SelectOption

from pydiscordbot.ext.config import settings


class BotModuleManager(commands.Cog):
    

    def __init__(self, app):
        self.app = app

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The module \"BotModuleManager\" are online!")

    # @commands.command()
    # @commands.has_role("admin")
    # async def available_modules(self, ctx):
    #     # TODO: fazer o available_extensions aparecer formatado
    #    await ctx.send(",".join(settings.AVAILABLE_MODULES))

    # @commands.command()
    # @commands.has_role("admin")
    # async def loaded_extensions(self, ctx):
    #     loaded_modules = [module.replace("pydiscordbot.ext.","") for module in self.app.extensions.keys()] 
    #     # TODO: fazer o available_extensions aparecer formatado
    #     await ctx.send(",".join(loaded_modules))

    @commands.command()
    @commands.has_role("admin")
    async def load_modules(self, ctx):
        try:
            loaded_modules = self.app.extensions.keys()
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in settings.MODULES.items():
                if module_path not in loaded_modules:
                    select_options.insert(
                        0,
                        SelectOption(label=module_name.title(), value=module_path, emoji="⚙️")
                    )
            msg = await ctx.send(
                "Select the module to be loaded into the bot:",
                components=[
                    SelectMenu(
                        custom_id="load_module",
                        placeholder=f"Choose up to {len(select_options)} modules",
                        max_values=len(select_options),
                        options=select_options
                    )
                ]
            )
            def check(m):
                return m.author == ctx.author
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(check=check, timeout=60)
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
                return None
            # Load the modules
            for module_path in selected_values:
                self.app.load_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been loaded: {', '.join(selected_labels)}")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")

    @commands.command()
    @commands.has_role("admin")
    async def unload_modules(self, ctx):
        try:
            loaded_modules = self.app.extensions.keys()
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in settings.MODULES.items():
                if module_path in loaded_modules:
                    select_options.insert(
                        0,
                        SelectOption(label=module_name.title(), value=module_path, emoji="⚙️")
                    )
            msg = await ctx.send(
                "Select the module to be unloaded from the bot:",
                components=[
                    SelectMenu(
                        custom_id="unload_module",
                        placeholder=f"Choose up to {len(select_options)} modules",
                        max_values=len(select_options),
                        options=select_options
                    )
                ]
            )
            def check(m):
                return m.author == ctx.author
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(check=check, timeout=60)
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
                return None
            # Load the modules
            for module_path in selected_values:
                self.app.unload_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been unloaded: {', '.join(selected_labels)}")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")


    @commands.command()
    @commands.has_role("admin")
    async def reload_modules(self, ctx):
        try:
            loaded_modules = self.app.extensions.keys()
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in settings.MODULES.items():
                if module_path in loaded_modules:
                    select_options.insert(
                        0,
                        SelectOption(label=module_name.title(), value=module_path, emoji="⚙️")
                    )
            msg = await ctx.send(
                "Select the module to be reloaded from the bot:",
                components=[
                    SelectMenu(
                        custom_id="reload_module",
                        placeholder=f"Choose up to {len(select_options)} modules",
                        max_values=len(select_options),
                        options=select_options
                    )
                ]
            )
            def check(m):
                return m.author == ctx.author
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(check=check, timeout=60)
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
                return None
            # Load the modules
            for module_path in selected_values:
                self.app.reload_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been reloaded: {', '.join(selected_labels)}")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")

    @reload_modules.error
    @unload_modules.error
    @load_modules.error
    async def extension_errors(self, ctx, error):
        try:
            error_msgs = {
                commands.ExtensionNotFound: f"This extension was not found.\nCheck the available modules using the "
                                            f"{settings.COMMAND_PREFIX}available_modules command.",
                commands.ExtensionAlreadyLoaded: f"This extension already loaded!",
                commands.NoEntryPointError: f"This extension can't be loaded! Please contact the system admin.",
                commands.ExtensionFailed: f"This extension cannot be loaded because an error was found in it."
                                          f"Please contact the system admin.",
                commands.ExtensionNotLoaded: f"This extension isn't loaded! You can check loaded extensions"
                                             f" using {settings.COMMAND_PREFIX}loaded_extensions"
            }
            if message := error_msgs.get(type(error.original)):
                await ctx.send(message)
        except AttributeError:
            pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRole):
            await ctx.send("You don't have the correct role for this command.")

