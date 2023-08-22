from tkinter import *
import time
# 创建窗口
win= Tk()
win.title("创建画布")
win.geometry("600x400")
# 创建Canvas
cv= Canvas(win,width=400,height=300,bg="white")
# 设置画布放置布局
cv.pack()
#输出文字
myStr = "welcome 欢迎"
C_T1 = cv.create_text(200, 30, text=myStr)
C_T2 = cv.create_text(200, 50, text=myStr, fill='blue')
C_T3 = cv.create_text(200, 90, text=myStr, fill='red',
                    font=('隶书',20))

for i in range(10):
    cv.move(C_T3,200-i*10,30)
    time.sleep(1)

# 显示主窗口
win.mainloop()