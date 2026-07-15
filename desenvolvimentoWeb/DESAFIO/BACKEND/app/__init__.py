from flask import Flask

from app.routes import tasks_bp
from .extensions import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///tasks.db',
    )

    db.init_app(app)
    app.register_blueprint(tasks_bp, url_prefix='/api')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    with app.app_context():
        db.create_all()
    return app