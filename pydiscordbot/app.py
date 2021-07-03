from discord.ext import commands

from pydiscordbot.ext.config import settings
from pydiscordbot.ext import bot, countdown


def create_app():
    # creating bot
    app = commands.Bot(command_prefix=settings.COMMAND_PREFIX)

    # Initiating extensions
    bot.init_app(app)
    countdown.init_app(app)

    return app.run(settings.TOKEN_BOT)
