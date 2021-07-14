from discord.ext import commands
from asyncio.exceptions import CancelledError, TimeoutError
from dislash import SelectMenu, SelectOption
from sqlalchemy.orm.exc import NoResultFound

from ext.config import settings
from ext import db
from ext.db.models import Module


class BotModuleManager(commands.Cog):

    def __init__(self, app):
        self.app = app
        if not self._module_in_db():
            self._insert_module_in_db()

    # Auxiliary methods
    def _insert_module_in_db(self):
        module = Module(
            name="BotModuleManager",
            path="ext.modules.modulemanager.botmodulemanager",
            disableable=False
        )
        db.session.add(module)
        db.session.commit()

    def _module_in_db(self):
        try:
            db.session.query(Module).filter(Module.name == "BotModuleManager").one()
            return True
        except NoResultFound:
            return False

    def _get_unloaded_modules(self):
        unloaded_modules = []
        app_modules = self.app.extensions.keys()
        for module_name, module_path in settings.MODULES.items():
            if module_path not in app_modules:
                unloaded_modules.append((module_name, module_path))
        return unloaded_modules

    def _get_loaded_modules(self):
        loaded_modules = []
        app_modules = self.app.extensions.keys()
        for module_name, module_path in settings.MODULES.items():
            if module_path in app_modules:
                loaded_modules.append((module_name, module_path))
        return loaded_modules

    # Command methods

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The BotModuleManager module are online!")

    @commands.command()
    @commands.has_role("admin")
    async def load_modules(self, ctx):
        try:
            # set select/dropdown options
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in self._get_unloaded_modules():
                select_options.insert(
                    0,
                    SelectOption(
                        label=module_name.title(),
                        value=module_path,
                        emoji="⚙️"
                    )
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
            # Load the modules
            for module_path in selected_values:
                self.app.load_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been loaded: {', '.join(selected_labels)}")
        except CancelledError:
            await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
        except TimeoutError:
            await msg.reply(f"⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
        except ModuleNotFoundError:
            await inter.reply(f"😿 Unknown error. Please contact the administrator. ")

    @commands.command()
    @commands.has_role("admin")
    async def unload_modules(self, ctx):
        try:
            # set select/dropdown options
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in self._get_loaded_modules():
                select_options.insert(
                    0,
                    SelectOption(
                        label=module_name.title(),
                        value=module_path,
                        emoji="⚙️"
                    )
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
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(
                check= (lambda m: m.author == ctx.author),
                timeout=60
            )
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                raise CancelledError()
            # Load the modules
            for module_path in selected_values:
                self.app.unload_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been unloaded: {', '.join(selected_labels)}")
        except CancelledError:
            await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
        except TimeoutError:
            await msg.reply("⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
        except ModuleNotFoundError:
            await inter.reply(f"😿 Unknown error. Please contact the administrator. ")


    @commands.command()
    @commands.has_role("admin")
    async def reload_modules(self, ctx):
        try:
            # set select/dropdown options
            select_options = [
                SelectOption(label="Cancel", value="cancel", emoji="❌")
            ]
            for module_name, module_path in self._get_loaded_modules():
                select_options.insert(
                    0,
                    SelectOption(
                        label=module_name.title(),
                        value=module_path,
                        emoji="⚙️"
                    )
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
            # Wait for a click on the menu that was sent.
            inter = await msg.wait_for_dropdown(
                check= (lambda m: m.author == ctx.author),
                timeout=60
            )
            # Tells which option was selected. 
            selected_options = inter.select_menu.selected_options
            selected_labels = [option.label for option in selected_options]
            selected_values = [option.value for option in selected_options]
            if "cancel" in selected_values:
                raise CancelledError()
            # Load the modules
            for module_path in selected_values:
                self.app.unload_extension(module_path)
            await inter.reply(f"👌 The following module(s) have been reloaded: {', '.join(selected_labels)}")  
        except CancelledError:
            await inter.reply("⚠️ The process was canceled because the cancel option was selected.")
        except TimeoutError:
            await msg.reply("⚠️ No modules were selected within the timeout (60 seconds). The process was aborted.")
        except ModuleNotFoundError:
            await inter.reply(f"😿 Unknown error. Please contact the administrator. ")

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