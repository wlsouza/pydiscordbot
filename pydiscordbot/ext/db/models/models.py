from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ...db import Base


class Guild(Base):

    __tablename__ = "guilds"

    # columns
    id = Column(Integer, primary_key=True)
    prefix = Column(String, default="$")

    #relationships
    guildmodules = relationship("GuildModule", back_populates="guild")

    def __repr__(self):
        return f"Guild(id={self.id}, prefix={self.prefix})"


class Module(Base):

    __tablename__ = "modules"

    # columns
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    disableable = Column(Boolean, nullable=False, default=True)
    emoji = Column(String)

    # relationships
    guildmodules = relationship("GuildModule", back_populates="module")

    def __repr__(self):
        return f"Module(id={self.id}, name={self.name})"


class GuildModule(Base):

    __tablename__ = "guildmodules"

    # columns
    id = Column(Integer,autoincrement=True, primary_key=True)
    guild_id = Column(Integer, ForeignKey("guilds.id"))
    module_id = Column(Integer, ForeignKey("modules.id"))
    active = Column(Boolean, nullable=False, default=True)

    #relationships
    guild = relationship("Guild", back_populates="guildmodules")
    module = relationship("Module", back_populates="guildmodules")

    def __repr__(self):
        return f"GuildModule(id={self.id})"



