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
  > <p align="center">
  >  <img src=".github/preview/bot_module_manager_preview.gif" width="500"/>
  > </p>
  
</details>

<details>
  <summary>
    <b>Management of guild modules</b>
  </summary>

  > This feature allows the owner of the guild that is using the bot to activate or deactivate the modules that the guild can use.  
  >
  > **How use:**  
  To use it, just send `$enable_modules` or `$disable_modules` and an interface like the one presented in the functionality above will appear for you to select the modules to be enabled or disabled.  
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
  To use it, just send `$change_prefix %` replacing the `%` with whatever character you want to use as a command prefix in your guild.  
  >
  >**Obs.** This functionality only affects the guild that executed the command. 
  >
  >**Obs2.** After changing the prefix, the bot will no longer respond to commands starting with `$` (default prefix), and will only respond to commands using the prefix informed in the exchange. 
</details>

### This template also has:
- Database connection using SQLAlchemy + SQLITE.
- Migrations using Alembic.
- Configuration management using Dynaconf.
- Factory pattern structure.

## :construction_worker: Installing and Running:

### ⬇️ How to download it:

This repository is a template, you can click on **Use this template** in the upper left to create GitHub repository based on this template.

### ⚙️ How to set up:

To use the project it is necessary to create a file called `.secrets.toml` with your bot's token and the database connection data. 
Notes:
  1. An example file is provided with the name "exemple.secrets.toml".
  2. I developed this template using sqlite, you can use whatever database you like, but you might need to modify some things.

If you want to change the environment to something other than "development" it is necessary to pass the desired env through the system variable `PYDISCORDBOT_ENV`.  
There are 2 simple ways to do this:

1. Create the `.env` file with the following content:
    `PYDISCORDBOT_ENV = "insert_the_environment_here(ex:PRODUCTION)"`.
2. Export the environment variable using the bash command: 
    On linux:
    ```bash
    export PYDISCORDBOT_ENV=INSERT_THE_ENVIRONMENT_HERE
    ```
    On Windows:
    ```bat
    set PYDISCORDBOT_ENV=INSERT_THE_ENVIRONMENT_HERE
    ``` 
### ✨️ How to start:

- Create a discord bot **[here](https://discord.com/developers/applications)**.
- Get your bot token.
- Invite your bot on servers using the following invite:
  https://discordapp.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot&permissions=8 
  (Replace `YOUR_APPLICATION_ID_HERE` with the application ID)
- Install the dependencies with the following command:
  ```bash
  pip install -r requirements.txt
  ```
- In the repository folder run the [app.py](pydiscordbot/app.py) file just as any other Python script (.py) file.
  ```bash
  python pydiscordbot/app.py
  ```
  Notes:  
    - It is recommended that you do all of the above process using a virtual environment. (You can read about it [here](https://docs.python.org/3/tutorial/venv.html).)


### Creating new modules.

  Soon...

## 🛠️ Dependencies
- [Python](https://www.python.org)
- [discord.py](https://discordpy.readthedocs.io/en/latest/) - An API wrapper for Discord written in Python.
- [dislash.py](https://dislashpy.readthedocs.io/en/latest/) - An extending library for discord.py that allows to build message components and slash commands.
- [dynaconf](https://www.dynaconf.com) - A configuration management library for Python.
- [sqlalchemy](https://www.sqlalchemy.org) - The Python SQL Toolkit and Object Relational Mapper (ORM).
- [alembic](https://alembic.sqlalchemy.org/en/latest/) -  A database migrations tool written by the author of SQLAlchemy.

## 💻 Authors

* **Wellington Lorenço de Souza**

See also the list of [contributors](https://github.com/wlsouza/pydiscordbot/graphs/contributors) who participated in this project.
