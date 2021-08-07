from discord.ext import commands
# from dislash import SelectMenu, SelectOption
# from asyncio.exceptions import CancelledError, TimeoutError
from sqlalchemy.orm.exc import NoResultFound

from ext.modules import Module
from ext.db import models
from ext.utils import checkers


class GuildConfig(Module):

    # Auxiliary methods

    def _init_guild_in_db(self, guild):
        #I used this method to find out if the guild already exists because
        #I didn't want to use a sqlite's specific exception. 
        # (since I intend to migrate to another db in the future)
        try:
            self.session.query(models.Guild).filter(
                models.Guild.id == guild.id
            ).one()
        except NoResultFound:
            guild = models.Guild(
                id = guild.id 
            )
            self.session.add(guild)
            self.session.commit()

            
    # Command methods        
    @commands.command()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), checkers.is_guild_owner())
    async def change_prefix(self, ctx, arg):
        try:
            new_prefix = arg.strip()
            guild = self.session.query(models.Guild).filter(
                models.Guild.id == ctx.guild.id
            ).one()
            guild.prefix = new_prefix
            self.session.commit()
            await ctx.send("👌 The prefix was changed!")
        except:
            self.session.rollback()
            await ctx.send("😿 The prefix could not be changed, please contact your system administrator.")

    # Listeners methods
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self._init_guild_in_db(guild)
