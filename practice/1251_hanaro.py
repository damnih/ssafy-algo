
import math
import heapq

# 가중치에 따른 최소 거리는 다익스트라~!

# 환경 부담금을 최소로 지불한대
# 고로 가중치는 거리에 존재함
# 거리는 root(dx^2 + dy^2)

# 즉 가중치는 이렇게 계산을 해서 넣어주고,
# 다음 갈 노드를 넣어주는 거임
#
# 즉 우선순위 큐에 넣는 게 (다음노드까지의거리, 다음노드) 이렇게 됨!!!
#
# 근데 모든 애들을 연결해야하는거 아님??
#
# 이거 근데 그냥
# 지금 내가 갈 수 있는 노드들(그냥 나머지 모든 노드들)
# 이렇게 되는 듯?
# 그리고 한번 연결하면 그 노드는 더 확인 ㄴㄴ
# 그니깐 visited 활용해서 그 노드 갔는지 안갔는지 체크해주면 되겠다


def dist_val(now, next):
    now_x, now_y = now
    next_x, next_y = next
    next_dist = (now_x - next_x) ** 2 + (now_y - next_y) ** 2
    return next_dist

# 근데 이거 굳이 루트 씌워줄 필요 없었네??



INF = float("inf")


N = int(input()) # 섬의 개수

island_list = []
# N개의 줄에 걸쳐서 x좌표 y좌표
island_x = list(map(int, input().split()))
island_y = list(map(int, input().split()))

for i in range(N):
    node_x = island_x[i]
    node_y = island_y[i]
    island = (node_x, node_y)
    island_list.append(island)

E = float(input())

visited = [0] * N # 어차피 0부터 섬들도 다 넣어놨기 때문에 이러는거 ㄱㅊㄱㅊ
# 나는 이걸 인덱스로 처리해서 약간 그 머냐 몇 번째 노드이면 방문했습니다
# 이런 식으로 노드의 번호를 만들어주고 싶엇는데 이거 가가ㄴ능함????
# 왜냐하면 내가 이런 식으로 하려면 약간 for문으로 돌려서 해야할거같은데
# 그러면 모든.. 상황에 대해 for문을 돌려야 하는 건가??

for idx in range(N):
    if visited[idx] != 0:
        continue



