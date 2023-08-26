

# 演示 如何使用 python的 debug功能

def fun(a,b):
    a = a*2
    b = b*3
    c = a + b
    return c


for i in range(1,10):
    k = i+7
    m = fun(i,k)

    print(m)