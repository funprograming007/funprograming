
#一个整数，它加上 100 后是一个完全平方数，再加上 168又是一个完全平方数，请问该数是多少

#9 = 3*3   16 = 4*4

# 8 判断是不是完全平方数  2 3 4 ,  8/2=4  2 3 4 5\

# 如果num是平方数 则 return True， 否则 return False
def is_square(num):
    for i in range(1, int(num/2) + 1):
        if( i * i == num):
            #print(f"{num}是一个平方数，他的平方根为 {i}")
            return True
    return False

for j in range(1,1000):
    if is_square(j+100) and is_square(j + 100 + 168):
        print(f"{j} 满足题目要求")

# 21  121=11*11  121+168=289=13*13




