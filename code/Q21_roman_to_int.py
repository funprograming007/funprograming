
#罗马数字的秘密
# 罗马       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# IV            4
# IX            9
# XL            40
# XC            90
# CD            400
# CM            900

# 求  III =3   IVX= 14  CDIM=1401

# 给定罗马数字 求解总数量， 预看下个字幕，碰到 I X C 三个字母 需要看下一个字母是不是预定的组合

map_roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC":90,
    "CD":400,
    "CM":900
}

input_str = "CDIM"

# i=0 len=3  i=1  i=2

i = 0
sum = 0
while(i<len(input_str)):
    # 判断i后面是否还有字母
    if i <= len(input_str) - 2:#还有字母
        two = input_str[i:i+2]
        if two in map_roman:
            sum += map_roman[two]
            i += 2
            #结束本次循环
            continue
    # 单个字母进行计算
    one = input_str[i:i+1]
    sum += map_roman[one]
    i += 1

print(f"{input_str}的值为{sum}")







