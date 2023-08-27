#有个闯关节目，目标是要穿越过一座山，团队中任何一个人穿越过去就算胜利，但要保证所有人能够存活、不挨饿。
#穿越这座山需要12天的时间，但每个人
#最多只能带上8天的粮食，并且每个人的饭量都相同，所带的食物全部是一样的，那么，如果换做是你来闯关，你认为最少需要几个人才能穿越过这座山？
#（返回出发地的路上需要粮食，返回出发地后不用粮食

# 举例法理解
# 假设1个走   最多前进4天
#       1       2     3     4     5     6     7    8    9   10   11   12（目的地）
#      P（7）  P（6） P（5） P（4）
#      四种走法：第一天回家 、 第二天回家、 第三回家 、 第四天回家

# 假设2个人走
#       1       2     3     4     5     6     7    8    9   10   11   12（目的地）
#      P1      P1     P1   P1
#      P2      P2     P2   P2
#     走法有多少种： 2个人都单独走的话  4 * 4 = 16
#                  2个人协作走：     P1第一天返回    P2 还有三种走法
#                                  P1第二天返回    P2 三种走法
#                                  P1第三天返回    。。。
#                                  P1第四天返回    。。。
# 假设5个人一起走

# 思路： 一次走一种情况： 走足够的次数就可以遍历所有可能的情况： 找出最优，最远的方案：

import random


def carry_num_all(temp):
    empty = 0
    keys = list(temp.keys())
    # 每个人消费了一份粮食
    for key in keys:
        empty += 8-temp[key]

    return empty


longest_day = 0
longest_steps = []

try_num = 10000
while(try_num>0):
    try_num -= 1
    steps = []
    steps.append(f"\n\n===========第{try_num}尝试================")
    number = 2
    people = {}
    day = 0
    for i in range(number):
        people[f"队员{i + 1}"] = 8  # 每个人携带的食物数量


    while(day<=12):
        #大家一起出发
        day += 1
        steps.append(f"------------第{day}天---------------")

        left_food = 0
        keys = list(people.keys())
        find_solution = False
        #每个人消费了一份粮食
        for key in keys:
            people[key] -= 1
            steps.append(f"{key} 前天一天")

            #是否可以成功到达
            if people[key] >= 12-day:
                day = 12
                steps.append(f"{key} 能够成功到达终点")
                find_solution = True
                break

            #要不要回家
            if people[key]-day-2 <0:
                leftnum = people[key] - day
                left_food += leftnum
                steps.append(f"{key} 粮食不足返程, 贡献出{leftnum}份食物")
                del people[key]

        if find_solution:
            break

        #概率问题 每个人都面临两个选择，要么继续前进，要么回家，本者不浪费的原则
        keys = list(people.keys())
        for key in keys:
            # 剩余粮食已够用
            if left_food >= carry_num_all(people):
                break

            if random.random()>0.5:#回家
                leftnum = people[key] - day
                left_food += leftnum
                steps.append(f"{key} 提前返程, 贡献出{leftnum}份食物")
                del people[key]


        #分配粮食
        keys = list(people.keys())
        for key in keys:
            if left_food>8-people[key]:
                left_food -= 8-people[key]
                people[key] = 8
            else:
                people[key] += left_food
                break

        if left_food>0:
            steps.append(f"分配食物后，还剩{left_food}份食物")

        steps.append(str(people))

        if len(people.keys())==0:
            steps.append("全体已返回")

            break
    if day > longest_day:
        longest_day = day
        longest_steps = steps

print(f"最长前进的天数为 {longest_day}")
print("\n".join(longest_steps))





