from discord.ext import commands
from pydiscordbot.ext.config import settings


class MainBot(commands.Cog):

    def __init__(self, app):
        self.app = app

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The {self.app.user.name} bot are online!")

    @commands.command()
    @commands.has_role("admin")
    async def available_modules(self, ctx):
        # TODO: fazer o available_extensions aparecer formatado
       await ctx.send(",".join(settings.AVAILABLE_EXTENSIONS))

    @commands.command()
    @commands.has_role("admin")
    async def loaded_extensions(self, ctx):
        loaded_extensions = str(self.app.extensions)
        # TODO: fazer o available_extensions aparecer formatado
        await ctx.send(loaded_extensions)

    @commands.command()
    @commands.has_role("admin")
    async def load_extension(self, ctx, extension: str):
        self.app.load_extension(f"pydiscordbot.ext.{extension}")
        await ctx.send(f"The module {extension} was loaded.")

    @commands.command()
    @commands.has_role("admin")
    async def unload_extension(self, ctx, extension: str):
        self.app.unload_extension(f"pydiscordbot.ext.{extension}")
        await ctx.send(f"The module {extension} was unloaded.")

    @commands.command()
    @commands.has_role("admin")
    async def reload_extension(self, ctx, extension: str):
        self.app.reload_extension(f"pydiscordbot.ext.{extension}")
        ctx.send(f"The module {extension} was reloaded.")

    @reload_extension.error
    @unload_extension.error
    @load_extension.error
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
        except Exception:
            raise

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRole):
            await ctx.send("You don't have the correct role for this command.")

    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content
        author = message.author
        channel = message.channel
        if not author.bot and content.startswith("salve"):
            await channel.send(f"Tá salvado {str(author).split('#')[0]}!")
