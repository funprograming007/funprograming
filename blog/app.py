
# Flask  容易学习的一个 python 建站的包， 使用且仅使用这个包， 目的让大家不要被大量的名词和技术所困扰

# 用户站点：    用户模块 =》 用户登录、用户注册、修改密码
#             博客模块 =》 新建博客、博客一览、博客详细、博客搜索、博客删除、博客评论
# 管理员站点：  用户管理 =》 用户查询、用户修改、用户删除
#             博客管理 =》 博客搜索、博客删除、博客修改

from flask import Flask, render_template

app = Flask(__name__)

# 用户部分
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/change_password")
def change_password():
    return render_template("change_password.html")


# 博客部分



@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)