#两个乒乓球队进行比赛，各出三人。甲队为 a,b,c三人，乙队为 x,y,z 三人。已抽签决定比赛名单。
#有人向队员打听比赛的名单。a 说他不和 x比，c 说他不和 x,z 比，请编程序找出三队赛手的名单

# a-->x  b-->y  c-->z   NG
#        b-->z  c-->y   NG
# a-->y  b-->x  c-->z   NG
#        b-->z  c-->x   NG
# a-->z  b-->x  c-->y   OK
#        b-->y  c-->x   NG

# 解题思路： 首先找出所有的比赛组合， 然后判断是否满足预设的条件，如果满足则打印出来

team_a = set(["a","b","c"])
team_b = set(["x","y","z"])

result=[]

for i in team_a:
    for j in team_b:
        # i和j进行比赛
        for m in team_a - set([i]):
            for n in team_b - set([j]):
                # m 和 n 进行比赛
                left_a = list(team_a - set([i,m]))[0] #team a剩下的最后一个人
                left_b = list(team_b - set([j,n]))[0] #team b剩下的最后一个人

                # i-->j m-->n left_a-->left_b

                match_result = [f"{i}{j}", f"{m}{n}", f"{left_a}{left_b}"]

                is_ok = True
                for pair in match_result:
                    if pair in ["ax","cx","cz"]:
                        is_ok = False

                if is_ok:
                    #print(f"{i}{j} {m}{n} {left_a}{left_b}")
                    result.append(match_result)

for i in range(len(result)):
    result[i].sort()
    result[i] = " ".join(result[i])


print(set(result))




