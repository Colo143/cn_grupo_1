from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.channel_bp import channel_bp
from .routes.error_handlers import errors


from .database import DatabaseConnection


def init_app():
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(user_bp, url_prefix = '/users')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(channel_bp, url_prefix = '/channels')
    app.register_blueprint(errors)

    return app