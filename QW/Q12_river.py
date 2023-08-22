import threading
import time

#羊，狼，菜过河。
#一个商人，带了一匹狼，一只羊，一筐菜。来到了一条大河边。现在商人只有一条船，而且每次只能带一样东西往返大河两岸。
#在商人不在的时候，狼会吃掉羊，羊会吃掉菜。如何才能让这三件东西完好无损的到达河对岸。

from util.gui import GUI
win = None

def startwin():
    global win
    win = GUI()
    win.add_item("wolf", 110, 30, "black")
    win.add_item("sheep", 110, 70, "red")
    win.add_item("vegetables", 110, 110, "blue")
    win.add_item("people", 110, 150, "green")
    win.add_line(200, 0, 200, 400, "red")
    win.add_line(400, 0, 400, 400, "red")
    win.root.mainloop()

thread = threading.Thread(target=startwin)
thread.start()

time.sleep(3)


side_a = set(["wolf", "sheep", "vegetables"])
side_b = set([])

def check(seta, which):
    setleft = seta - set([which])

    if "wolf" in setleft and "sheep" in setleft:
        return False
    if "sheep" in setleft and "vegetables" in setleft:
        return False

    return True


times = 0
last_thing = ""
while(len(side_b) != 3):
    if times%2 == 0:#a->b
        find_solution = False
        for i in side_a-set([last_thing]):
            if check(side_a,i):
                side_a = side_a - set([i])
                side_b = side_b.union(set([i]))
                print(f"商人带着{i}渡河去对面")

                win.move_item(f"{i}", 400, 0)
                win.move_item("people", 400, 0)

                last_thing = i
                find_solution = True
                break
        if not find_solution:
            print(f"商人自己渡河去对面")
            win.move_item("people", 400, 0)
    else:       #b->a
        find_solution = False
        if not check(side_b, ""):
            for i in side_b-set([last_thing]):
                if check(side_b, i):
                    side_b = side_b - set([i])
                    side_a = side_a.union(set([i]))
                    print(f"商人带着{i}回来")

                    win.move_item(f"{i}", -400, 0)
                    win.move_item("people", -400, 0)

                    last_thing = i
                    find_solution = True
                    break
        if not find_solution:
            print(f"商人自己从河对面回来")
            win.move_item("people", -400, 0)

    times = times+1
    time.sleep(2)

win.show_msg("finished!")