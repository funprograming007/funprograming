

# 寻找最长回文字串
# cbabad

# 解题： 子串问题1是不是回文  对称的字符串叫做回文字串 aba  bcdcb aa  b
# 思路： 1. 寻找所有子串  2. 判断是不是回文 3.取最长的那个


temp = "cbabad"

longest_len = 0
longest_substr = ""

#遍历所有的子串
for i in range(len(temp)): #以每一个字符作为开头进行遍历 temp[i:j] 左闭右开
    for j in range(i+1, len(temp)+1):
        x = temp[i:j]

        if len(x) <= longest_len:
            continue

        #判断子串是不是回文的
        if x == x[::-1]:  # x = abc  x[::-1] = cba
            if longest_len < len(x):
                longest_len = len(x)
                longest_substr = x

print(f"最长回文子串的长度为{longest_len}，该子串为{longest_substr}")





