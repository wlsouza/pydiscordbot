from discord.ext import commands

from starbot.ext.config import settings
from starbot.ext import bot
from starbot.ext import brhue


def create_app():
    # creating bot
    app = commands.Bot(command_prefix=settings.COMMAND_PREFIX)

    # Initiating extensions
    bot.init_app(app)
    brhue.init_app(app)

    return app.run(settings.TOKEN_BOT)
