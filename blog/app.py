import sqlite3

# Flask  容易学习的一个 python 建站的包， 使用且仅使用这个包， 目的让大家不要被大量的名词和技术所困扰

# 用户站点：    用户模块 =》 用户登录、用户注册、修改密码
#             博客模块 =》 新建博客、博客一览、博客详细、博客搜索、博客删除、博客评论
# 管理员站点：  用户管理 =》 用户查询、用户修改、用户删除
#             博客管理 =》 博客搜索、博客删除、博客修改

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.config['SECRET_KEY'] = "fdlsjkafjieri7987"

# 用户部分
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    del session['id']
    return redirect(url_for("login"))

@app.route("/do_login", methods=["POST"])
def do_login():
    form = request.form
    name = form.get("name", "")
    password = form.get("password", "")

    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("select * from user where name=? and password = ?", [name, password])
    result = cur.fetchall()
    if len(result) >0: #找到用户
        session['id'] = result[0][0]
        return redirect(url_for("index"))
    else:#找不到
        return render_template("login.html",error="用户名或者密码错误")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/do_register", methods=["POST"])
def do_register():
    form = request.form
    name = form.get("name","")
    password = form.get("password","")
    password2 = form.get("password2", "")

    if name=="" or password != password2:
        return render_template("register.html", error="用户名为空或者密码不一致")

    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("insert into user(name, password) values(?,?)",[name,password])
    conn.commit()

    return redirect(url_for("login"))

@app.route("/change_password")
def change_password():
    return render_template("change_password.html")


# 博客部分
@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/do_add",methods=["POST"])
def do_add():
    form = request.form
    title = form.get("title","")
    content = form.get("content","")

    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("insert into blog(title, content,uid) values(?,?,?)", [title, content,session['id']])
    conn.commit()

    return redirect(url_for("index"))

@app.route("/delete")
def delete():
    args = request.args
    id = args.get("id","")

    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("delete from blog where id = ?", [id])
    conn.commit()
    return redirect(url_for("index"))


@app.route("/")
def index():
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("select * from blog where uid = ? order by id desc", [session['id']])
    blogs = cur.fetchall()

    return render_template("index.html",blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)