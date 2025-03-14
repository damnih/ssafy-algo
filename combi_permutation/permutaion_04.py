# 카드 5장을 뽑으면 종료
# 연속된 3개가 나오면 counting

card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True


def recur(cnt):
    if cnt == 5:
        # 연속된 3개가 나오면 카운트하는게 여기 들어가야 함
        if count_three():
            result += 1
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()