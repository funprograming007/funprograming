import os
import sqlite3
import sys

# Flask  容易学习的一个 python 建站的包， 使用且仅使用这个包， 目的让大家不要被大量的名词和技术所困扰

# 用户站点：    用户模块 =》 用户登录、用户注册、修改密码
#             博客模块 =》 新建博客、博客一览、博客详细、博客搜索、博客删除、博客评论
# 管理员站点：  用户管理 =》 用户查询、用户修改、用户删除
#             博客管理 =》 博客搜索、博客删除、博客修改

from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, abort


base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

app.config['SECRET_KEY'] = "fdlsjkafjieri7987"

from controller_user import controller_user
app.register_blueprint(controller_user)
from controller_blog import controller_blog
app.register_blueprint(controller_blog)


if __name__ == "__main__":
    app.run(debug=True)