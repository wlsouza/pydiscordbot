from .ping import Ping


def init_app(app):
    """
    I'm using init_app to call the app.load_extension function because if I just call the setup
    function directly, the extension name would not be added to the __extensions attribute of the app.
    """
    app.load_extension(__name__)


def setup(app):
    module = Ping(
        app = app,
        name = "Ping",
        path = "ext.modules.ping",
        disableable = True,
        emoji = "🏓" 
    )
    app.add_cog(module)
