from discord.ext import commands
# from dislash import SelectMenu, SelectOption
# from asyncio.exceptions import CancelledError, TimeoutError
from sqlalchemy.orm.exc import NoResultFound, 

from ext.modules import Module
from ext.db import models
from ext.utils import checkers


class GuildConfig(Module):

    # Auxiliary methods

    def _init_guild_in_db(self, ctx):
        guild = models.Guild(
            id = ctx.guild.id 
        )
        self.session.add(guild)
        self.session.commit()

            
    # Command methods        
    @commands.Cog.command()
    async def change_prefix(self, ctx):
        raise NotImplementedError("To be implemented")

    # Listeners methods

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        raise NotImplementedError("To be implemented")
