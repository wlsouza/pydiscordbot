from pydiscordbot.ext.modules.guildmodulemanager.guildmodulemanager import GuildModuleManager
from .guildmodulemanager import GuildModuleManager

def init_app(app):
    app.load_extension(__name__)

def setup(app):
    module = GuildModuleManager(
        app = app,
        name = "GuildModuleManager",
        path = "ext.modules.guildmodulemanager",
        disableable = False,
        emoji = None 
    )
    app.add_cog(module)

