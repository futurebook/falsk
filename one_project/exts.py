from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# 操作数据库绑定
db = SQLAlchemy()
# 发送邮件绑定
mail = Mail()
