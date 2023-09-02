from tools.MyWin import MyWin

if __name__ == '__main__':
    a = MyWin()
    a.add_input("name","姓名")
    a.add_input("age", "年龄")
    a.add_input("file", "选择文件","File")
    a.add_input("dir", "选择目录","Path")
    a.start()
