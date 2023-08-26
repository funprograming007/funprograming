
#最长公共回文子串
# abadefg   ugfasjgabad   最长子串 abad  最长回文子串 aba

# 问题1： 求最长公共子串
# 问题2： 子串还是回文的
# 解题思路： 1. 先求出所有的公共子串 2. 判断是不是回文 3. 打印最长的那个

str1 = "ababadefg"
str2 = "ugfasjgababad"

longest_len = 0
longest_str = ""

for i in range(len(str1)):
    for j in range(i+1, len(str1)+1):
        temp = str1[i:j]
        if len(temp) < longest_len:
            continue

        #是不是公共子串,如果短的都不在，后续长肯定不在，减少运算量
        if not temp in str2:
            break

        if temp[::-1] == temp:
            longest_len = len(temp)
            longest_str = temp

print(f"最长公共回文子串长度为{longest_len} 子串是{longest_str}")



