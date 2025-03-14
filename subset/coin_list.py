coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target//coin
    cnt += possible_cnt
    target -= coin *target

