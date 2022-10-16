from exts import db
from datetime import datetime

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class UserModel(db.Model):
    # 定义表名为users
    __tablename__ = 'user'
    # 将id设置为主键，并且默认是自增长的
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # name字段，字符类型，最大的长度是50个字符
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)

# class UserExtension(db.Model):
#     __tablename__ = 'user_extension'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     school = db.Column(db.String(200))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     # db.backref
#     # 1.在反向引用时如果需要传递一些参数， 就要用到这个函数，如果不传递参数直接写字符串就行
#     # 2.uselist=False：代表反向引用时，不是一个列表，而是一个对象
#     user = db.relationship("UserModel", backref=db.backref('extension', uselist=False))
#
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#
#     # 1.外键的类型一定要看所引用的类型
#     # 2.db.ForeignKey('表明.字段名')
#     # 3.外键是数据库层面的不推荐直接再ORM层面使用
#     #     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     #     # relationship:
#     # 1.第一个参数是模型的名字， 必须要和模型的名字保持一致
#     # 2.backref（back reference）：代表反向引用，代表对方访问时候的字段名称
#     author = db.relationship('User', backref='articles')

class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    author = db.relationship("UserModel", backref="questions")

class AnswerModel(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    question = db.relationship("QuestionModel",backref=db.backref("answers", order_by=create_time.desc()))
    author = db.relationship("UserModel",backref="answers")

