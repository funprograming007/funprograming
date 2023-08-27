

# 完美匹配
# 四种括号  [] {} <> ()
# 成功案例  []()  ([]{})
# 失败案例  [(])  {)

# 学习队列的概念：  FIFO   First In First Out  先进先出     水管     单向流动  左边进 右边出    | -》 -》  |
#                FILO   First In Last  Out  先进后出     水杯     进口就是出口  左边进 左边出  -》 | 《-      |停止，
# 类似于子弹夹  最先按进去的子弹 是不是最后弹出来

# list  append尾巴上加  pop 尾巴上拿

# 解题思路： 如果碰到 [ { < (  按进去， 如果碰到 ] } > ) 出仓匹配， 如果不匹配 失败， 如果全部匹配完成后 数组为空，匹配成功

# []()        数组为空                      []
#             看第一个字符 [                 [ "[" ]   压入
#             看第二个字符 ]                 []        弹出 "["， 看是否和 ] 匹配， 发现匹配  继续
#             看第三个字符 (                 [ "(" ]   压入
#             看第四个字母 )                 []        弹出 "("， 看是否和 ) 匹配， 发现匹配  字符串结束+并且数组为空  判断成功

temp = "[(])"
stack = []

map_brackets = {
    "]" : "[",
    ">" : "<",
    "}" : "{",
    ")" : "("
}

# 假设用户只输入 以上8种符号
for i in temp:
    # 左边的括号
    if i not in map_brackets:
        stack.append(i)
        continue
    else:
        # 右边括号来了
        if len(stack) >0:
            m = stack.pop()
            if m == map_brackets[i]:
                continue
            else:
                print("failed")
                break

        else:
            print("failed")
            break

if len(stack) == 0:
    print("success")




