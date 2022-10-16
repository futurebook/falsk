# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 设置DB_URI
SQLALCHEMY_DATABASE_URI = DB_URI
# 是否开启sql修改警告
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 就相当于加密的密钥
SECRET_KEY = '123'

# 邮箱配置
# 项目中使用的是qq邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# 调试时开启，上线可关闭，作用是在下方打印出提示信息
MAIL_DEBUG = True
# 注册接受邮箱
MAIL_USERNAME = "qq邮箱账号"
# POP3/SMTP服务的密码
MAIL_PASSWORD = "服务的密码"
# 默认发送者
MAIL_DEFAULT_SENDER = "qq邮箱账号"
