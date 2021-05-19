# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:44
#@Author: 赵雯
#@File : __init__.py.py

from flask import Flask
from .extensions import config_extensions
from .config import Config

# 工厂函数
def create_app(app_name):
    app = Flask(app_name)
    app.config.from_object(Config)
    config_extensions(app)
    return app
