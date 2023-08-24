

#用蒙特卡洛法 求 圆周率 Pi的值 3.1415926.....
# 圆的面积 = Pi x r x r  计算公式
# 蒙特卡洛

import random
def generate(f1,f2):
    return (f2-f1)*random.random() + f1

try_num = 5000000
in_circle = 0
in_all = try_num

while(try_num > 0):
    #生产靶点的随机 坐标
    target_x = generate(-1,1)
    target_y = generate(-1,1)

    #判断是否落在圆内
    if target_x*target_x + target_y*target_y <=1:
        in_circle += 1

    #继续尝试
    try_num -= 1

# 圆面积=Pi*1*1=Pi  正方形的面积是 2*2=4
# 圆面积/正方形的面积 = in_circle（落在圆里的靶点数目）/try_num（落在正方形里的靶点数）

pi = 4 * in_circle / in_all

print(f"Pi的值近似等于 {pi}")