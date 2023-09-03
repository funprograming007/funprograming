from flask import Blueprint, render_template, session, redirect, url_for, request

from blog import db
from blog.wrapper import login_required, admin_required

controller_user = Blueprint("user",__name__,url_prefix="/user")
@controller_user.route("/show")
def show():
    return "show user"

@controller_user.route("/login")
def login():
    return render_template("login.html")

@controller_user.route("/logout")
@login_required
def logout():
    del session['id']
    return redirect(url_for("user.login"))

@controller_user.route("/do_login", methods=["POST"])
def do_login():
    form = request.form
    name = form.get("name", "")
    password = form.get("password", "")


    result = db.query_sql("select * from user where name=? and password = ?", [name, password])
    if len(result) >0: #找到用户
        session['id'] = result[0][0]
        return redirect(url_for("blog.index"))
    else:#找不到
        return render_template("login.html",error="用户名或者密码错误")


@controller_user.route("/register")
def register():
    return render_template("register.html")

@controller_user.route("/do_register", methods=["POST"])
def do_register():
    form = request.form
    name = form.get("name","")
    password = form.get("password","")
    password2 = form.get("password2", "")

    if name=="" or password != password2:
        return render_template("register.html", error="用户名为空或者密码不一致")


    db.exec_sql("insert into user(name, password) values(?,?)",[name,password])


    return redirect(url_for("user.login"))

@controller_user.route("/change_password")
@login_required
def change_password():
    return render_template("change_password.html")

@controller_user.route("/user_list")
@admin_required
def user_list():
    users = db.query_sql("select * from user")

    return render_template("user_list.html", users=users)

@controller_user.route("/user_delete")
@admin_required
def user_delete():
    args = request.args
    id = int(args.get("id","0"))

    db.exec_sql("delete from user where id =?",[id])

    return redirect(url_for("user.user_list"))