import flask
from flask.helpers import url_for
import JMBlog
import models
from flask import request, render_template
from werkzeug.utils import redirect

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

    return redirect(url_for("account.Login"))


@bp.route("/login/")
def Login():
    return render_template("login.html")


@bp.route("/login/confirm", methods=["POST"])
def LoginConfirm():
    account_list = JMBlog.db.session.query(models.Account).all()
    for account in account_list:
        print(account.id)
        print(account.id)

        if account.id == request.form.get(
            "id"
        ) and account.password == request.form.get("password"):
            print("2")
            return render_template("account_info.html", account=account)

    print("3")
    return redirect(url_for("main.Index"))