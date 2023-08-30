
# 求最大的路径总和
#       1
#      2  3
#    4   5  6

#  全部走左边 1 2 4 = 7
#  全部走右边 1 3 6 = 10
#  先左后右   1 2 5 = 8
#  先右后左   1 3 5 = 9
#  一共四种走法， 最大值 10 走法是 1 3 6

#  解题思路， 找规律， 递归解决问题， 从下往上走
#           1(10)
#        2(7)    3(9)
#    4(4)   5(5)    6(6)
#     j  j+1
# i   1  0  0
# i+1 2  3  0
#     4  5  6

#  i, j  的左边 i+1,j  右边是   i+1,j+1

maze = [
    [1,0,0],
    [8,3,0],
    [4,5,6]
]

def maxroute(i,j):
    if i == len(maze)-1:
        return maze[i][j]

    left = maxroute(i+1,j)
    right = maxroute(i+1,j+1)

    # 左右选择大的和自己相加得到自己向下所有的最大值
    return max(left,right) + maze[i][j]



print(f"最大长度是{maxroute(0,0)}")
