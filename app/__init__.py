from flask import Flask
from config import Config
from app.extensions import db
from flask_migrate import Migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extension
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    # blueprints
    from app.main import bp as main_bp
    from app.admin import bp as admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.route("/index")
    def index():
        return "Hello"

    return app
