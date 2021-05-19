# -*- coding:utf-8 -*-
# Created by ZhaoWen on 2020/10/12

from app import create_app
from app.extensions import db

def test_app(app_name):
    app = create_app(app_name)
    app.app_context().push()
    db.init_app(app)
    return app,db