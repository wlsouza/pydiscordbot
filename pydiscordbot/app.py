from discord.ext import commands
from dislash import SlashClient

from ext.config import settings
from ext.modules import  botmodulemanager, guildmodulemanager, guildconfig, ping
from ext.utils import checkers
from ext import db


def create_app():
    
    # creating bot
    app = commands.Bot(command_prefix=checkers.get_prefix)
    slash = SlashClient(app)

    # create database
    db.init_app()

    # Initiating required modules
    botmodulemanager.init_app(app) # Required module
    guildmodulemanager.init_app(app) # Required module
    guildconfig.init_app(app) # Required module

    # Initiating secondary modules
    ping.init_app(app)

    return app.run(settings.TOKEN_BOT)

if __name__ == "__main__":
    create_app()




