from discord.ext import commands

from ext import modules

class Countdown(modules.Module):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")




