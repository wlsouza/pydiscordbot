from discord.ext import commands
from dislash import SlashClient

from ext.config import settings
from ext.modules import modulemanager, countdown
from ext.utils import checkers
from ext import db
from ext.db import models



def create_app():
    # creating bot
    app = commands.Bot(command_prefix=checkers.get_prefix)
    slash = SlashClient(app)

    # create database
    db.init_app()

    # Initiating modules
    modulemanager.init_app(app) # Most Important module
    countdown.init_app(app)

    # m1 = models.Module(name="test", path="teste", emoji="❌")

    # g1 = models.Guild(id=860716845194543104, prefix="!")

    # db.session.add(g1)

    # db.session.commit()

    return app.run(settings.TOKEN_BOT)

if __name__ == "__main__":
    create_app()
