'''

# 1qnxj 10Rkwl
# 1부터 10까지

numset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

full_subset = []
for num in range(1<<10):
    subset = []
    for i in range(10):
        if num & (1 << i):
            subset.append(numset[i])
    full_subset.append(subset)

# 근데 나는 이걸 재귀에서 가지치기를 이용해 하고 싶어...

subset.pop()

'''

# numset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

arr = [i for i in range(1, 11)]
visited = []

# level: N개의 원소를 모두 고려하면
# branch: 집합에 해당 원소를 포함 시키는경우/ 안시키는 경우
# 누적값
# - 부분집합의 총합
# - 부분집합에 포함된 원소들

def dfs(cnt, total, subset):
    # 1. total이 10이면 출력해라
    if total == 10:
        print(subset)
        return

    # 2. total이 10을 넘으면 가지치기하자
    if total > 10:
        return

    if cnt == 10:
        # cf. total값 서치를 여기서 하는 것은
        # 카운트 10까지 다 간 다음에 하겠다는 말과 똑같음
        # 미리 쳐내는 게 아니야 불가능해
        return

    # 포함 하는 경우
    #
    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])
    # 포함 안하는 경우
    # 포함 안하니깐 토탈과 부분집합에 변화가 없음
    dfs(cnt + 1, total, subset)


dfs(0, 0, [])

# 재귀 DFS 백트래킹은 전부 같은 맥락이라고 생각하면 됨