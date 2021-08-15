from discord.ext import commands

from ext.modules import Module
from ext.utils import checkers

class Ping(Module):

    @commands.command()
    @checkers.module_is_enabled_in_guild()
    async def ping(self, ctx):
        await ctx.send("pong!")




