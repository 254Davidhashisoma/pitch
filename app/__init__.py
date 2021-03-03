from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import login_manager
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' 
def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # # Setting the config
    from .requests import configure_request
    configure_request(app)

    return app