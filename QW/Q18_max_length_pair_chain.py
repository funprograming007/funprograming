

#问题： 数字接龙
#描述： 若干个小朋友每个人想两个不同的数字，一个小一个大， 如果一个小朋友的最大值小于另外一个小朋友的最小值，他们就可以连接
#      给定若干个小朋友的数字，求最多多少小朋友可以连起来

temp =  [[1,2],[3,4],[2,3],[5,7]]

def find_longes(pair):
    #如果少于一个小朋友 返回1
    if len(pair) <=1:
        return 1

    #按照最小值进行排序 [[1,2],[2,3],[3,4]]
    pair = sorted(pair)

    longest = 0
    longest_who = []

    #尝试从第i个小朋友寻找最长可能的接龙数
    for i in range(len(pair)):
        len_once = 1

        who = []
        now = pair[i]
        who.append(now)

        #从第i+1个小朋友开始搜索
        for j in range(i+1, len(pair)):
            next = pair[j]
            if now[1] < next[0]:
                len_once += 1
                who.append(next)
                now = next

        if longest < len_once:
            longest = len_once
            longest_who = who

    return longest,longest_who

number,whos = find_longes(temp)
print(f"最长的接龙小朋友数为 {number}, 他们的数为{whos}")





