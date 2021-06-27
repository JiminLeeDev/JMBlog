import flask

from flask.templating import render_template

bp = flask.Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def Index():
    return render_template("index.html")
