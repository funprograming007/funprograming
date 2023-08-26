
#一球从 100 米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第 10次落地时，共经过多少米？第 10 次反弹多高？

# 100米 第一次落地 经过 100米  第一次反弹 50米
#       第二次落地 经过 100+50+50=200米 第二次反弹 25米
#       第三次落地 经过 200+25+25=250米 第三次反弹 12.5米

sum_length  =  0
height = 100
bounce = 0

num = 10

for i in range(num):
    sum_length += height
    if i>0:
        sum_length += height
    bounce = height/2
    height = height/2

print(f"{num}次落地时，共经过{sum_length}米，第{num}次反弹高度为{bounce}米")



