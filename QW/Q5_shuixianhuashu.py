#打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
#例如：153是一个“水仙花数”，因为 153=1的三次方＋5的三次方＋3的三次方

# 153   1   5   3
# 153%10 = 3  15%10 = 5  1%10=1取模这个操作
from math import floor
def is_shuixianhuashu(num):
    temp = num
    sum = 0
    while(num>0):
        tail = num % 10
        sum += tail * tail * tail

        num = floor(num / 10);

    if sum == temp:
        return True
    else:
        return False

for i in range(1,1000):
    if is_shuixianhuashu(i):
        print(f"找到一个水仙花数 {i}")


