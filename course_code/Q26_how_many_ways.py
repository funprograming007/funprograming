

# 有一个3x3的方各自，小人在左上方， 小人只能向右走或者向下走，求小人走到右下角有多少种走法？

# 解题思路：  小人到达任何一个格子的路径数 = 小人到达该格子上方格子的路径数目 + 小人道道该格子左边方格子的路径数

#     j=0  1   2
#i=0   1   1   1
#  1   1   2   3
#  2   1   3   6

#m行 n列的情况
m=4
n=8

x = [[0]*n  for i in range(m)]

for j in range(n):
    x[0][j] = 1
for i in range(m):
    x[i][0] = 1

for i in range(1,m):
    for j in range(1,n):
        x[i][j] = x[i-1][j] + x[i][j-1]


for i in x:
    print(i)