# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:45
#@Author: 赵雯
#@File : extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate



#创建对象
db = SQLAlchemy()
migrate = Migrate()


#初始化
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app,db)


