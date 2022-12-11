from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# import config

db = SQLAlchemy()
migrate = Migrate()

# def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
#     return value.strftime(fmt)

def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)
    app.config.from_envvar('APP_CONFIG_FILE')
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models



    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
