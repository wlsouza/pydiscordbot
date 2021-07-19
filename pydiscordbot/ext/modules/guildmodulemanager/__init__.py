from .guildmodulemanager import GuildModuleManager

def init_app(app):
    """
    I'm using init_app to call the app.load_extension function because if I just call the setup
    function directly, the extension name would not be added to the __extensions attribute of the app.
    """
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
