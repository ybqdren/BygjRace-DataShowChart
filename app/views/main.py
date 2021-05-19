# -*- coding:utf-8 -*-
#@Time : 2020/9/20 14:48
#@Author: 赵雯
#@File : main.py

from flask import Blueprint
from flask import render_template
from app.models import Tbl_Video_Game_Sales
from app import create_app
from app.extensions import db

# 创建蓝图
main_print = Blueprint('main_print',__name__)

# 图像切换
@main_print.route('/charts/changeView')
def change_View():
    game_sale = Tbl_Video_Game_Sales.query.order_by(Tbl_Video_Game_Sales.Global_Sales.desc()).first()
    return render_template('/main/changeView-chart.html',game_sale = game_sale)

# 字符云
@main_print.route('/charts/wordCount')
def word_Count():
    db.init_app(create_app('app'))
    game_name = list(set(db.session.query(Tbl_Video_Game_Sales.Platform).order_by(Tbl_Video_Game_Sales.Global_Sales.desc()).limit(100)))
    return render_template('/main/wordCount-chart.html',game_name = game_name)

# 玫瑰饼图
@main_print.route('/charts/rosePie')
def charts_rosePie():
    game = Tbl_Video_Game_Sales.query.filter(Tbl_Video_Game_Sales.Platform == 'PS3').order_by(Tbl_Video_Game_Sales.Global_Sales.desc()).all()[:10]
    return render_template('/main/rosePie-chart.html',game = game)

# 饼图
@main_print.route('/charts/pie')
def charts_pie():
    game = Tbl_Video_Game_Sales.query.filter(Tbl_Video_Game_Sales.Platform == 'PS3').order_by(Tbl_Video_Game_Sales.Global_Sales.desc()).all()[:10]
    return render_template('/main/pie-chart.html',game = game)

# 雷达图
@main_print.route('/charts/radar')
def charts_radar():
    game = Tbl_Video_Game_Sales.query.filter(Tbl_Video_Game_Sales.Platform == 'Wii').all()[:3]
    return render_template('/main/radar-chart.html',game = game)

# 折线图
@main_print.route('/charts/line')
def charts_line():
    game = dict()
    for y in range(1999,2011,1):    #2000~2010
        game[y] = Tbl_Video_Game_Sales.query.filter(Tbl_Video_Game_Sales.Year == y).count()
    return render_template('/main/line-chart.html',game = game)


# 柱状图
@main_print.route('/charts/bar')
def charts_bar():
    game_sale = Tbl_Video_Game_Sales.query.first()
    if( game_sale != None):
        return  render_template('/main/bar-chart.html',game_sale = game_sale)


@main_print.route('/')
def index():
    return render_template('/main/index.html')