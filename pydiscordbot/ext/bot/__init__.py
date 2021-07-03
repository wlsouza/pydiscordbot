from starbot.ext.bot.mainbot import MainBot


def init_app(app):
    app.load_extension(__name__)


def setup(app):
    app.add_cog(MainBot(app))
