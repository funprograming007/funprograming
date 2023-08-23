#黑洞数又称陷阱数，是类具有奇特转换特性的整数。任何一个数字不全相同的整数，经限“重排求差”操作，
#总会得到某一个或一些数，这些数即为黑洞数。“重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
#举个例子，3位数的黑洞数为495.
#验证4位数的黑洞数为6174。

# 123   1 2 3 组成  321 - 123 = 198
# 198   1 9 8 组成  981 - 189 = 792
# 792   7 9 2 组成  972 - 279 = 693
# 693   6 9 3 组成  963 - 369 = 594
# 。。。。。。
# 495   4 9 5 组成  954 - 459 = 495 黑洞数
import random
def convert(number):
    digitals = list(map(int,str(number)))
    digitals.sort(reverse=True)
    maxnum = 0
    for i in digitals:
        maxnum=maxnum*10 + i

    digitals.sort()
    smallnum = 0
    for i in digitals:
        smallnum = smallnum*10 + i

    return maxnum - smallnum

init_num = random.randint(1000,9999) # 前后包含的

while(True):
    print(init_num)
    j = convert(init_num)

    if init_num == j:
        print(f"黑洞数是{j}")
        break
    else:
        init_num = j





