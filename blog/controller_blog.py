from flask import Blueprint, render_template, request, redirect, url_for, session

from blog import db
from blog.wrapper import login_required

controller_blog = Blueprint("blog",__name__,url_prefix="/blog")
@controller_blog.route("/show")
def show():
    return "show user"

@controller_blog.route("/add")
@login_required
def add():
    return render_template("add.html")

@controller_blog.route("/do_add",methods=["POST"])
@login_required
def do_add():
    form = request.form
    title = form.get("title","")
    content = form.get("content","")


    db.exec_sql("insert into blog(title, content,uid) values(?,?,?)", [title, content,session['id']])


    return redirect(url_for("blog.index"))

@controller_blog.route("/delete")
@login_required
def delete():
    args = request.args
    id = args.get("id","")

    db.exec_sql("delete from blog where id = ?", [id])

    return redirect(url_for("blog.index"))


@controller_blog.route("/edit")
@login_required
def edit():
    args = request.args
    id = args.get("id", "")

    data = db.query_sql("select * from blog where id = ?",[id])

    return render_template("edit.html", blog=data[0])

@controller_blog.route("/do_edit",methods=['POST'])
@login_required
def do_edit():
    form = request.form
    id = form.get("id","")
    title = form.get("title","")
    content = form.get("content","")

    db.exec_sql("update blog set title=?, content=? where id=?",[title,content,id])
    return redirect(url_for("blog.index"))

@controller_blog.route("/init")
def init():
    db.exec_sql("create table if not exists user(id integer primary key autoincrement, name, password)")
    db.exec_sql("create table if not exists blog(id integer primary key autoincrement, title, content,uid interger)")
    return "init ok!"

@controller_blog.route("/")
@login_required
def index():
    args = request.args
    key = args.get("key","")
    page = int(args.get("page","1"))
    if page < 1:
        page = 1
    number_per_page = 10

    blogs = db.query_sql("select * from blog where (title like ?  or content like ?) and uid = ? order by id desc limit ?,?",
                         [f"%{key}%", f"%{key}%",session['id'], (page-1)*number_per_page, number_per_page])

    return render_template("index.html",blogs=blogs, page=page)