

import tkinter as tk
from tkinter import Menu, filedialog, END, messagebox


class MyWin:

    def __init__(self,title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("600x600")

        #self.interface()
        self.items = []
        self.objects = {}
        self.hook=  lambda x: 1

    def start(self):
        """"界面编写位置"""

        for i in self.items:
            tk.Label(self.root, text=i["label"]).pack()
            if i["type"] == "Entry":
                self.objects[i["name"]] = tk.Entry(self.root)
                self.objects[i["name"]].pack()
            if i["type"] == "File":
                self.objects[i["name"]] = tk.Entry(self.root)
                self.objects[i["name"]].pack()
                tk.Button(self.root, text='Select', command=self.get_file(i["name"])).pack()
            if i["type"] == "Path":
                self.objects[i["name"]] = tk.Entry(self.root)
                self.objects[i["name"]].pack()
                tk.Button(self.root, text='Select', command=self.get_path(i["name"])).pack()
            if i["type"] == "Text":
                self.objects[i["name"]] = tk.Text(self.root, width=68, height=10)
                self.objects[i["name"]].pack()

        self.Button0 = tk.Button(self.root, text="Submit", command=self.process)
        self.Button0.pack()

        # self.objects["log"] = tk.Text(self.root, width=68, height=10)
        # self.objects["log"].pack()

        self.root.mainloop()

    def get_file(self,name):
        def wrapper():
            path = filedialog.askopenfilename(title='请选择文件')
            e = self.objects[name]
            e.delete(0, END)
            e.insert(0, path)

        return wrapper

    def get_path(self, name):
        def wrapper():
            """注意，以下列出的方法都是返回字符串而不是数据流"""
            # 返回一个字符串，且只能获取文件夹路径，不能获取文件的路径。
            path = filedialog.askdirectory(title='请选择一个目录')

            # 生成保存文件的对话框， 选择的是一个文件而不是一个文件夹，返回一个字符串。
            # path = filedialog.asksaveasfilename(title='请输入保存的路径')

            e = self.objects[name]
            e.delete(0, END)
            e.insert(0, path)
        return wrapper


    def add_input(self,name,label,type="Entry"):
        self.items.append({"type":type, "name":name, "label":label})

    def get_value(self,name):
        #print(type(self.objects[name]))
        if isinstance(self.objects[name], tk.Text):
            return self.objects[name].get('0.0', 'end')
        return self.objects[name].get()

    def process(self):
        """按钮事件,获取文本信息"""
        dict = {}
        for key in self.objects.keys():
            dict[key] = self.get_value(key)
        self.hook(dict)
    def set_hook(self,f):
        self.hook = f

    def show_msg(self,str,title="INFO"):
        messagebox.showinfo(title, str)


def process(dict):
    print(dict)

if __name__ == '__main__':
    a = MyWin("test")
    a.add_input("name", "姓名")
    a.add_input("age", "年龄")
    a.add_input("file", "选择文件", "File")
    a.add_input("dir", "选择目录", "Path")
    a.add_input("content", "文章", "Text")

    a.set_hook(process)
    a.start()
