from discord.ext import commands
from sqlalchemy.orm.exc import NoResultFound

from ext.db import session
from ext.db.models import Guild
from ext.config import settings


def get_prefix(client, message): 
    try:
        guild = session.query(Guild).filter(Guild.id==message.guild.id).one()
        return guild.prefix
    except NoResultFound:
        return settings.default_command_prefix

def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

