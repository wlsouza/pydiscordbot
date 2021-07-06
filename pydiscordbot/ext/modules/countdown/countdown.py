import random

from discord.ext import commands


class CountDown(commands.Cog):

    def __init__(self, app):
        self.app = app

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"The {self.__class__.__name__} module are online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     author = message.author
    #     channel = message.channel
    #     if not author.bot and str(author) == settings.RAMIN_ID:
    #         phrases = [
    #             "Perguntei para o Matheus e ele disse que quem mandou a última msg leva linguiça no churrasco!",
    #             "Alerta! Chat exclusivo para seres humanos.",
    #             "Olha o burguês safado falando bosta de novo."
    #         ]
    #         await channel.send(random.choice(phrases))

    # @commands.Cog.listener()
    # async def on_voice_state_update(self, member, before, after):
    #     channel = member.voice.channel
    #     voice_client = member.guild.voice_client
    #     if not before.afk and after.afk:
    #         # ficou afk
    #         print("ficou afk")
    #         await self.app.join_voice_channel(channel)
    #         # TODO: Finish it.
    #         await voice_client.disconnect()
    #     elif before.afk and not after.afk:
    #         # saiu do afk
    #         print("saiu do afk")
    #     elif not before.self_mute and after.self_mute:
    #         # se mutou
    #         print("se mutou")
    #         await channel.connect()
    #         # TODO: Finish it.
    #     elif before.self_mute and not after.self_mute:
    #         # se desmutou
    #         print("se desmutou")
    #         await voice_client.disconnect()


