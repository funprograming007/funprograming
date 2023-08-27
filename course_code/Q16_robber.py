

#你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
#影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
#如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

house = [1, 3, 2, 1]

def get_max(temp):  # 返回 [maxnum, [选择的数字] ]
    #如果小于2个数字 一共就是两种拿法
    if len(temp)<=2:
        return max(temp),[max(temp)]

    #如果大于2个数
    #如果拿第一个， 必须跳过第二数
    max_rest1, choosed1 = get_max(temp[2:])
    max1 = temp[0] + max_rest1

    #如果不拿第一个
    max2, choosed2 = get_max(temp[1:])

    choosed_number = []
    if max1 > max2:
        choosed1.append(temp[0])
        choosed_number = choosed1
    else:
        choosed_number = choosed2

    return max(max1,max2), choosed_number

max_money, choosed = get_max(house)
print(f"最大金额为 {max_money}, 选择的数字为{choosed}")
