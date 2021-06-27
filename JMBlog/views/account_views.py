import flask
import JMBlog
import models

from flask import request, render_template

bp = flask.Blueprint("account", __name__, url_prefix="/account/")


@bp.route("/register")
def Register():
    return render_template("register.html")


@bp.route("/register/confirm", methods=["POST"])
def RegisterConfirm():
    account = models.Account(
        id=request.form.get("id"),
        password=request.form.get("password"),
        nickname=request.form.get("nickname"),
    )

    try:
        JMBlog.db.session.add(account)
        JMBlog.db.session.commit()
    except:
        print("Validation is failed.")

    return render_template("index.html")
