

#（古典题）鸡兔同笼，头共10，足共28，鸡兔各几只？

# 鸡的数量 从 1只 到 9只  答案只可能在 9个数字当中产生

for num_chicken in range(1,10):
    if (num_chicken*2 + (10-num_chicken)*4) == 28:
        print(f"鸡的数量为{num_chicken}，兔子的数量为{10-num_chicken}")

# 6*2+4*4 = 16+12 = 28
