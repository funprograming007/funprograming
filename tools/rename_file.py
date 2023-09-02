import os

from tools.MyWin import MyWin


def process(dict):
    try:
        log = ""
        for filename in os.listdir(dict["dir"]):
            if filename.endswith(dict["suffix"]):
                newfilename = filename.replace(dict["origin"],dict["replace"])
                if newfilename!=filename:
                    os.rename(dict["dir"]+"/"+filename, dict["dir"]+"/"+newfilename)
                    log += f"{filename} 重命名为 {newfilename}\n"

        a.show_msg("修改文件如下:\n"+log,"成功")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    a = MyWin("文件名替换")
    a.add_input("dir", "选择目录","Path")
    a.add_input("suffix", "文件后缀")
    a.add_input("origin", "原字符")
    a.add_input("replace", "替换字符")
    a.set_hook(process)
    a.start()
