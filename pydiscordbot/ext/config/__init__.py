from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="STARBOT",
    settings_files=["settings.toml", ".secrets.toml"],
    load_dotenv=True,
    environments=True,
    env_switcher="STARBOT_ENV"
)

print(f"Config iniciada em modo: {settings.current_env}")

# def init_app(app):
#     pass
