# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:46
#@Author: 赵雯
#@File : __init__.py.py

from .main import main_print

# 封装
DEFAULT_BLUEPRINT = {
    (main_print,'')
}

#蓝图注册
def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,prefix=prefix)