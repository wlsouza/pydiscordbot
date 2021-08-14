# pydiscordbot 🤖
> A public multi-purpose bot that serves as the template for you to make your bot.  

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.9](https://img.shields.io/badge/python-_>=_3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

This repository is a template that you can use to start your own discord bot.  
I made this template so that everyone can start their own bot already with a good structure, making it easy to maintain and scale.

### Features already implementeds:
<details open>
  <summary>
    <b>Management of bot modules</b>
  </summary>
  
  > This feature allows you to load or unload the bot's modules (or Cogs, as you prefer to call it), that is, the bot owner (and only him) can in a simple way, unload a module for **all guilds** that are using the bot.  
  See how:  
  GIF here
</details>

<details>
  <summary>
    <b>Management of guild modules</b>
  </summary>

  > This feature allows the owner of the guild that is using the bot to activate or deactivate the modules that the guild can use.  
  >
  > **How use:**  
  To use it, just send ```$enable_modules``` or ```$disable_modules``` and an interface like the one presented in the functionality above will appear for you to select the modules to be enabled or disabled.  
  >
  >**Obs.** Unlike the previous one this feature does not affect everyone who is using the bot, it only affects the guild that executed the command.
</details>

<details>
  <summary>
    <b>Command prefix change</b>
  </summary>

  > This feature allows the guild owner to select which prefix he will use when sending a command to the bot.  
  >
  > **How use:**  
  To use it, just send ```$change_prefix %``` replacing the ```%``` with whatever character you want to use as a command prefix in your guild.  
  >
  >**Obs.** This functionality only affects the guild that executed the command. 
  >
  >**Obs2.** After changing the prefix, the bot will no longer respond to commands starting with ```$``` (default prefix), and will only respond to commands using the prefix informed in the exchange. 
</details>

### This template also has:
- Database connection using SQLAlchemy + SQLITE.
- Migrations using Alembic.
- Configuration management using Dynaconf.
- Factory pattern structure.

## :construction_worker: Installing and Running

## 🛠️ Dependencies
* [Python](https://www.python.org)
* [discord.py](https://discordpy.readthedocs.io/en/latest/) - An API wrapper for Discord written in Python.
* [dislash.py](https://dislashpy.readthedocs.io/en/latest/) - An extending library for discord.py that allows to build message components and slash commands.
* [dynaconf](https://www.dynaconf.com) - A configuration management library for Python.
* [sqlalchemy](https://www.sqlalchemy.org) - The Python SQL Toolkit and Object Relational Mapper (ORM).
* [alembic](https://alembic.sqlalchemy.org/en/latest/) -  A database migrations tool written by the author of SQLAlchemy.

## 💻 Authors

* **Wellington Lorenço de Souza**

See also the list of [contributors](https://github.com/wlsouza/pydiscordbot/graphs/contributors) who participated in this project.
