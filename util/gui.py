import tkinter as tk
import threading
from time import sleep
from tkinter import messagebox
#event = threading.Event()


class GUI:
    cv = None
    lock = threading.Lock()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('演示窗口')
        self.width = 600
        self.height = 400
        self.fontsize = 20
        self.root.geometry(f"{self.width}x{self.height}")

        self.object = {}
        self.cv = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        # 设置画布放置布局
        self.cv.pack()
        self.move = {}
        self.interface()


    def show_msg(self,str):
        messagebox.showinfo('INFO', str)

    def add_item(self,name,init_x, init_y, color):
        self.object[name] = self.cv.create_text(init_x, init_y, text=name,font=('tahoma',self.fontsize),fill=color)

    def move_item(self,name,x,y):
        self.lock.acquire()
        if name not in self.move:
            self.move[name] = []
        self.move[name].append([x,y])
        self.lock.release()

    def abs_move_item(self, name, new_x, new_y):
        # Get the current object position
        x, y, *_ = self.cv.bbox(self.object[name])
        # Move the object
        self.move_item(name, new_x - x, new_y - y)

    def add_line(self,x1,y1,x2,y2,color):
        self.cv.create_line(x1, y1, x2, y2, fill=color)
    def interface(self):
        self.start()

    def event(self):
        '''按钮事件，一直循环'''
        while True:
            sleep(1)
            #event.wait()
            self.lock.acquire()
            for key in self.move.keys():
                if len(self.move[key])>0:
                    for one in self.move[key]:
                        self.cv.move(self.object[key], one[0], one[1])
                    self.move[key] = []
            self.lock.release()

    def start(self):
        #event.set()
        T1 = threading.Thread(target=self.event, daemon=True)
        T1.start()

    def stop(self):
        #event.clear()
        self.w1.insert(1.0, '暂停'+'\n')

    def conti(self):
        #event.set()
        self.w1.insert(1.0, '继续'+'\n')


if __name__ == '__main__':
    win = GUI()
    win.add_item("wolf", 110, 30, "black")
    win.add_item("sheep", 110, 70, "red")
    win.add_item("vegetables", 110, 110, "blue")
    win.add_item("people", 110, 150, "green")
    win.add_line(200, 0, 200, 400, "red")
    win.add_line(400, 0, 400, 400, "red")

    #win.move_item("wolf", 100, 0)
    win.move_item("wolf", 400, 0)
    win.move_item("sheep", 400, 0)
    win.move_item("vegetables", 400, 0)
    win.move_item("people", 400, 0)

    win.root.mainloop()
