from discord.ext import commands
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_ 

from ext import db
from ext.db.models import Module

class Countdown(commands.Cog):

    name = "Countdown"
    path = "ext.modules.countdown"
    disableable = True
    emoji = "⏰" 

    def __init__(self, app):
        self.app = app
        self.session = db.Session()
        self._init_module_in_db()

    # Auxiliary methods

    def _init_module_in_db(self):
        try:
            module = self.session.query(Module).filter(or_(Module.name == self.name, Module.path == self.path)).one()
            module.name = self.name
            module.path = self.path
            module.disableable = self.disableable
            module.emoji = self.emoji
            self.session.commit()
        except NoResultFound:
            module = Module(
                name=self.name,
                path=self.path,
                disableable=self.disableable,
                emoji=self.emoji
            )
            self.session.add(module)
            self.session.commit()

    def _module_in_db(self):
        try:
            self.session.query(Module).filter(Module.name == "Countdown").one()
            return True
        except NoResultFound:
            return False

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The {self.__class__.__name__} module are online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")




