
from discord.ext import commands
from sqlalchemy import or_
from sqlalchemy.orm.exc import NoResultFound

from ext.db import Session
from ext.db import models


class Module(commands.Cog):

    def __init__(self, app, name, path, disableable, emoji):
        self.app = app
        self.name = name
        self.path = path
        self.disableable = disableable
        self.emoji = emoji
        self.session = Session()
        self._init_module_in_db()

    def _init_module_in_db(self):
        try:
            db_module = (
                self.session.query(models.Module)
                .filter(
                    or_(
                        models.Module.name == self.name,
                        models.Module.path == self.path
                    )
                ).one()
            )
            db_module.name = self.name
            db_module.path = self.path
            db_module.disableable = self.disableable
            db_module.emoji = self.emoji
            self.session.commit()
        except NoResultFound:
            db_module = models.Module(
                name=self.name,
                path=self.path,
                disableable=self.disableable,
                emoji=self.emoji
            )
            self.session.add(db_module)
            self.session.commit()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The {self.name} module are online!")
