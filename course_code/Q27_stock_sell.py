

#假设一个股票若干天的价格
#条件：你有一次买入和卖出的机会，请你设计一个算法来计算可以获得的最大收益。

#股价：            [2, 1 ,5, 4, 9]
#本日卖出所得最大：   0  0  4  3  8
# 题目解析: 1块买入 9块卖出 得到收益为8
# 令 n = 0       最大收益为0
#    n = 1       最大收益为0
#    n = 2       5-2=3  5-1=4  如果本日股价大于以往的价格，把以往的最大收益加上本日股价增幅，所有和的最大值就是本日的最大收益
#    n = 3       4-2=2  4-1=3  最大值为3
#    n = 4       9-2=7  9-1=8 9-5+4=8 9-4+3=8 最大收益 8

# 每日股价
price = [2, 1 ,5, 4, 9]

# 本日卖出能获取的最大收益,全部初始化为0
max_profit = [0] * len(price)

max_profit[0] = 0

for i in range(1,len(price)):
    max_number = 0
    for j in range(i):
        if price[i] >= price[j]:
            # 获取最大的那个收益增幅加上以往的最大值
            max_number = max(max_number, max_profit[j]+ price[i]- price[j])

    max_profit[i] = max_number

print(f"每日卖出收益最大值：{max_profit}")
print(f"卖出收益最大值为：{max(max_profit)}")







