from .botmodulemanager import BotModuleManager

def init_app(app):
    app.load_extension(__name__)

def setup(app):
    app.add_cog(BotModuleManager(app))

