from flask import Flask, Response, request, session, g
from flask_migrate import Migrate
from models import *
from blueprints import *
import config
from exts import *

app = Flask(__name__)
app.config.from_object(config)
# 把app绑定到db上
db.init_app(app)
# 把zpp绑定到mail上
mail.init_app(app)

migrate = Migrate(app, db)
# 加载蓝图
app.register_blueprint(user_bp)
app.register_blueprint(qa_bp)

@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫user的变量，他的值是user这个变量
            # setattr(g, 'user', user)
            g.user = user
        except:
            g.user = None

@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
