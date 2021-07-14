from ext.modules.modulemanager import botmodulemanager

def init_app(app):
    app.load_extension(__name__)

def setup(app):
    app.add_cog(botmodulemanager.BotModuleManager(app))
    # TODO: insert guildmodulemanager to can initiate both modules at once.

