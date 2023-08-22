
#题目：输入两个正整数m和n，求其最大公约数和最小公倍数。

# 最大公约数  6 9 他们的最大公约数是 3，尝试从 6 5 4 3 2 1 依次尝试。
# 最小公倍数  6 9 他们的最小公倍数是 18，尝试从 6 6+6 6+6+6 依次尝试，直到找到能同时被6和9 整除的数
#最大公约数
def max_gongyue(m,n):
    smaller = min(m,n)
    while(smaller>1):
        if m % smaller == 0 and n % smaller == 0:
            return smaller
        smaller -= 1
    return 1
def min_gongbei(m,n):
    smaller = min(m,n)
    temp = smaller
    while(True):
        if smaller % m == 0 and smaller % n ==0:
            return smaller
        smaller += temp
m = 6
n = 9
print(f"{m}和{n}的最大公约数是{max_gongyue(m,n)}")
print(f"{m}和{n}的最小公倍数是{min_gongbei(m,n)}")