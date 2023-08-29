

# 爬楼梯 n 楼， 一次爬1楼或2层楼， 问一共有多少终爬法

# n = 1    爬的种类   【1】         一种
# n = 2              【1 1】 【2】 二种
# n = 3              【1 1 1】 【1 2】 【2 1】 三种

# 解题思路： n>3 情况
#          如果第一次选择爬1楼   爬n-1楼的爬法
#              第一次选择爬2楼   爬n-2楼的爬法

#n=4       如果第一次爬1楼  【1】    还有3楼要爬    【1 1 1】 【1 2】 【2 1】
#                          【 1 1 1 1】 【 1 1 2】 【1 2 1】
#           如果第一次爬2楼 【2】    还有2楼要爬     【1 1】 【2】
#                           【2 1 1】 【2 2】

def climb(n):
    if n == 1:
        return 1,[[1]]
    if n == 2:
        return 2,[[1,1],[2]]

    #返回第一次爬1楼的方法数 + 第一次爬2楼的方法数
    num1, arr1 = climb(n-1) #以1开头
    num2, arr2 = climb(n-2) #以2开头

    for i in range(len(arr1)):
        arr1[i].insert(0,1)
    for i in range(len(arr2)):
        arr2[i].insert(0,2)

    #数组合并
    arr_all = [*arr1, * arr2]

    return num1+num2, arr_all

for i in range(1,10):
    num,ways = climb(i)
    print(f"爬 {i} 楼的爬法数有 {num}种,分别为{ways}")




