

#你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
#影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
#如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。



# 解题思路：
#    50%拿1     50%拿2       不能拿4  = 3
#               50%不拿2     肯定拿4  = 5
#    50%不拿1   50%拿3        肯定拿4  = 7
#              50%不拿3      50%拿2    不能拿4 = 2
#                           50%不拿2   肯定拿4 = 4

import random


plot_data = []
for times in range(1,101):
    try_num = times

    biggest_num = 0
    biggest_result = []

    while(try_num>0):
        try_num -= 1

        house = [1,3,2,4]
        result = []
        money_all = 0
        while(len(house)>0):
            if random.random() > 0.5: #拿
                temp = house.pop(0)
                money_all += temp
                result.append(temp)
                if len(house)>0:
                    house.pop(0)
            else: #不拿
                house.pop(0)

        if money_all>biggest_num:
            biggest_num = money_all
            biggest_result = result

    print(f"获取的最大总金额为{biggest_num}, 选择的金额列表为{biggest_result}")

    plot_data.append([times, biggest_num])

from matplotlib import pyplot as plt

plt.plot([x[0] for x in plot_data],[x[1] for x in plot_data])

plt.show()

