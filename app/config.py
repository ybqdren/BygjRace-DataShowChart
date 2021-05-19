# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:45
#@Author: 赵雯
#@File :
# config.py

import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql://root:666666@127.0.0.1:3306/race_flask'   #os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

