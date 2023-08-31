import sqlite3


def query_sql(sql,param=[]):
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute(sql,param)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def exec_sql(sql,param=[]):
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute(sql, param)
    conn.commit()
    conn.close()
