from flask import g, redirect, url_for
from functools import wraps


def login_required(func):
    # @wraps这个装饰器不能忘记写，不然得到的返回值的属性可能失真（例如属性名称变成wrapper）
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))

    return wrapper