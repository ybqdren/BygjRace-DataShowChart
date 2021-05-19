# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:51
#@Author: 赵雯
#@File : manage.py

from app import create_app
from app.views import config_blueprint
from flask_script import Manager
from flask_migrate import MigrateCommand
from flask_script import Server

app = create_app('app')
config_blueprint(app)
manager = Manager(app)
manager.add_command("runserver",Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()