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
