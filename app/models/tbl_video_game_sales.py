# -*- coding:utf-8 -*-
#@Time : 2020/9/22 16:07
#@Author: 赵雯
#@File : tbl_video_game_sales.py

from app.extensions import db

class Tbl_Video_Game_Sales(db.Model):
    __tablename__ = 't_video_game_sales'
    Rank = db.Column(db.String(255),primary_key=True)   #销售排名
    Name = db.Column(db.String(255))     #游戏名称
    Platform = db.Column(db.String(255))    #该游戏发布平台
    Year = db.Column(db.Integer)    #发布年份（1980-2016）
    Genre = db.Column(db.String(255))   #游戏类型
    Publisher = db.Column(db.String(255))    #出版公司
    NA_Sales = db.Column(db.DECIMAL(255,2))  #北美区域销量（以百万为单位计数）
    EU_Sales = db.Column(db.DECIMAL(255,2))  #欧美区域销量（以百位为单位计数）
    JP_Sales = db.Column(db.DECIMAL(255,2))  #日本区域销量（以百位为单位计数）
    Other_Sales = db.Column(db.DECIMAL(255,2))   #其他国家销量（以百位为单位计数）
    Global_Sales = db.Column(db.DECIMAL(255,2))   #全球销量（以百位为单位计数）
