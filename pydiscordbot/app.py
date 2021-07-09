from discord.ext import commands
from dislash import SlashClient

from ext.config import settings
from ext.modules import modulemanager, countdown

from ext import db
from ext.db import models


def create_app():
    # creating bot
    app = commands.Bot(command_prefix=settings.COMMAND_PREFIX) #TODO: implement get_prefix from db
    slash = SlashClient(app)

    # Initiating modules
    #db.init_app()

    # Initiating modules
    modulemanager.init_app(app) # Most Important module
    countdown.init_app(app)

    return app.run(settings.TOKEN_BOT)

if __name__ == "__main__":
    create_app()
