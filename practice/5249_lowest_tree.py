# import sys
# sys.stdin = open("5249_input.txt", "r")

# 최소신장트리는 그거임
# 그래프가 주어지면 거기서 가장 작은 가중치를 가진 애들을 선택해서 이어나가는 건데
# 사이클이 되지 않도록, 단방향으로만 가는거임

'''
3

2 3
0 1 1
0 2 1
1 2 6

4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''

# 대표자를 찾아주는 함수
def get_ref(x):
    if parent[x] == x:
        return x
    # 만약 자기자신이 아니라면
    parent[x] = get_ref(parent[x])
    return parent[x]


def union(x, y):
    refx = get_ref(x)
    refy = get_ref(y)

    if refx == refy:
        # 이미 같은 그룹임
        return

    # 만약 다르다면,, 대표자를 같게 해주면 그게 바로 같그룹임
    # 나는 일정한 규칙을 만들어줫어
    # 더 작은 놈을 대표로 만들어주는 거임 ㅋ
    if refx < refy:
        parent[refy] = refx
    if refx > refy:
        parent[refx] = refy


def draw_MST(edge_list):
    edge_cnt = 0
    edge_weight = 0

    # 간선인지 아닌지 여부를 확인할
    # 간선 그려주는 인접행렬이나 만들어주자 ㅋ
    # adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    # 위의 인접 행렬이 visited 역할을 해줄 거임

    for line in edge_list:
        n1, n2, w = line

        # 간선을 다 그려준 경우에 간선은 몇개? 정점개수 -1
        if edge_cnt == V:  # 정점의 개수가 V+1개니깐 여기선 V여야함
            # 간선의 가중치를 모두 더해 출력 ㅇㅇ
            # print(f"#{tc} {edge_weight}")
            return edge_weight

        # 간선을 그어주기 위해 지금 나는 얘네가 연결되어있는지 여부를 확인할거야
        # 만약 같은 그룹에 있지 않다면 = 연결 안되어있다면
        # if adj_matrix[n1][n2] == 0:
        ref1 = get_ref(n1)
        ref2 = get_ref(n2)
        if ref1 != ref2:
            # 연결이 안되어있는데 방문한 적도 없다면,,!

            # 간선을 연결해주고
            # 같은 그룹이라고 만들어줘!!!
            # 그리고 간선의 수를 셀 거니깐 올려줘!!!
            union(n1, n2)
            edge_cnt += 1
            edge_weight += w
            # adj_matrix[n1][n2] = w
            # adj_matrix[n2][n1] = w
            # 이제 이게 visited 역할을 해줄 거임 !!
            # 이 visited 확인은 어디서 해줘야 한다? 이 유니언을 묶어주기 전이다~~~


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())
    edge_list = []
    parent = [i for i in range(V + 1)]

    for line in range(E):
        n1, n2, w = map(int, input().split())
        edge_list.append((n1, n2, w))
    # print(edge_list)

    edge_list.sort(key = lambda x : x[2])
    # print(edge_list) # 잘됨

    # 근데 이 뒤로 어케해야,, 잘 선택하는걸까,,

    ans = draw_MST(edge_list)
    print(f"#{tc} {ans}")



    # 아 그니깐 사실
    # 나는 그냥 지금까지 간선의 정보만 저장한거지
    # 진짜로 그래프를 그린 게 아님 !!!!
    # 이제 선택하면서 그래프를 그려줄 거임
    # 엣지리스트에 저장한 정보들은 결국 시작점, 끝점, 가중치 이렇게 되는거잖아?
    # 가중치는 이미 활용했어 그 순으로 정렬
    # 그 말은 가중치가 적은 순으로 먼저 그래프를 찍 찍 그어주겠다는 뜻임
    #
    # 그니깐 결국
    # 내가 간선을 그어줄 그 두 정점이 연결되어있는지 아닌지 여부를 확인하기 위해
    # 겟 ㄷ루트 함수를 써주고
    # 다른 루트를 가졌음이 판명나는 경우
    # 일단 얘네 사이의 간선을 그어주고, 루트가 같아지게끔 유니언 해주면 됨!!!
    # 그렇게 돌면서
    # 그은 간선의 수가 왜 그거 ㅇㅇㅇ 정점보다 하나 적어지면
    # 단방향의 트리는 완성된거임
    # 거기서 멈추고 완성된 그림의 트리를 반환하면 될듯
    # 아ㅔㅔ

