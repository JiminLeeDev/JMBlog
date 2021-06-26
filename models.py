from flask.helpers import flash
from sqlalchemy.orm import backref
from JMBlog import db


class Account(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    post = db.relationship(
        "Post", db.backref("post_list", cascade="all, delete-orphan")
    )
    comment = db.relationship(
        "Comment", db.backref("comment_list", cascade="all, delete-orphan")
    )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    account = db.relationship(
        "Account", db.backref("account_list", cascade="all, delete-orphan")
    )
    comment = db.relationship(
        "Comment", db.backref("comment_list", cascade="all, delete-orphan")
    )


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    account = db.relationship(
        "Account", db.backref("account_list", cascade="all, delete-orphan")
    )
    post = db.relationship(
        "Post", db.backref("post_list", cascade="all, delete-orphan")
    )
