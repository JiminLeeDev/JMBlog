from flask.helpers import flash
from sqlalchemy.orm import backref
from JMBlog import db


class Account(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    comment_id = db.Column(
        db.Integer, db.ForeignKey("comment.id", ondelete="CASCADE"), nullable=True
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=True
    )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    comment_id = db.Column(
        db.Integer, db.ForeignKey("comment.id", ondelete="CASCADE"), nullable=True
    )


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
