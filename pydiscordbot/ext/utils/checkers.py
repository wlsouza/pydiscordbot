from discord.ext import commands
from sqlalchemy.orm.exc import NoResultFound

from ext.config import settings
from ext.db import models
from ext.db import session


def get_prefix(client, message): 
    try:
        guild = session.query(models.Guild).filter(models.Guild.id==message.guild.id).one()
        return guild.prefix
    except NoResultFound:
        return settings.default_command_prefix

def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

def module_is_enabled_in_guild():
    def predicate(ctx):
        try:
            enabled = (
                session.query(models.GuildModule)
                .join(models.Module)
                .filter(
                    models.GuildModule.guild_id == ctx.guild.id,
                    models.Module.name == ctx.cog.name,
                    models.GuildModule.enabled == True
                ).one()
            )
            return True
        except NoResultFound:
            return False
    return commands.check(predicate)
