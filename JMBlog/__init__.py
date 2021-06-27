import flask
import flask_migrate
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()


def create_app():
    app = flask.Flask(__name__)

    app.config.from_object("JMBlog.config")
    db.init_app(app)
    migrate.init_app(app, db)

    import models
    from .views import main_views, account_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(account_views.bp)

    return app
