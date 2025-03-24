def make_set(ㅜ):
    # 1~6까지의 원소가 있다고 가정, 총 n개의 집합을 생성
    # --> 각 원소의 부모(!= 대표자) (대표자와 부모는 다른 개념임)를 자기 자신으로 초기화
    parents = [i for i in range(N+1)]
    ranks = [0] * (N + 1) # rank를 모두 0으로 초기화
    # 이걸 나중에 하나씩 추가할때마다, 다시말해, 집합이 하나씩 생성될때마다 rank를 하나씩 올려줌
    return parents, ranks



# 이 서로소 연산을 좀 줄이기 위한 비기가 몇 개 있는데 바로
# 1. 경로압축
# 2. 랭크 활용

# 경로압축은 언제 일어나느냐? find_set이다!!!


# 할 때마다, 모든 노드의 대표자를 변경하자!!!
# way 1
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]] # 경로 압축
        x = parents[x]
    return x

# way 2
# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     # 경로 압축(path comprehension)을 통해 X의 부모를 대표자로 변경
#     parents[x] = find_set(parents[x])


# 3. x, y를 하나의 집합으로 묶는 것..
def union(x, y):
    # 일단 하나의 집합으로 묶으려면..
    # 같은 집합인지 다른 집합인지 확인부터 해야해
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 같다면,,
    if rep_x == rep_y:
        return # 걍 같은 집합이면 그대로 끝
    # 아니라면..
    # 합치러 가야지...
    # 문제에 따라 우선되는 집합으로 합쳐주면 됨!!
    # if rep_x < rep_y:
    #     parents[rep_y] = rep_x
    # if rep_x > rep_y:
    #     parents[rep_x] = rep_y
    # 같은 집합으로 합쳐준다는 뜻은 이 대표자가 같다는 뜻임!!!!!
    # 그러니깐 이렇게 해주는 거엿음!!!!1

    # 여기서,, 랭크가 작은 쪽으로 병합해준다!!!
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        # 랭크가 같다면 한 쪽으로 병합하고 아무거나 랭크 증가시킨다
        parents[rep_y] = rep_x
        rank[rep_x] += 1


N = 6
parents, ranks = make_set(N)
