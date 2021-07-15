from discord.ext import commands
from sqlalchemy.orm.exc import NoResultFound

from ext import db
from ext.db.models import Module

class Countdown(commands.Cog):

    def __init__(self, app):
        self.app = app
        self.session = db.Session()
        if self._module_in_db():
            self._update_module_in_db()
        else:
            self._insert_module_in_db()

    # Auxiliary methods
    def _insert_module_in_db(self):
        module = Module(
            name="Countdown",
            path="ext.modules.countdown",
            disableable=True,
            emoji="⏰"
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




