# pq는 우선순위 큐


def prim(start_node):
    pq = [(0, start_node)] # 시작점은 가중치가 0이다!!! 라는 뜻과 같음
    MST = [0] * V # visited랑 동일

    min_weight = 0 # 최소 비용 저장

    while pq:
        weight, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면,  패스
        if MST[node]:
            continue

        # 이런 식으로 뽑고 나서 바꿔주는 식으로 해줘야함
        MST[node] = 1
        min_weight += weight

        # BSF의 경우 갈 수 있는 경우를 확인했자낭
        for next_node in range(V):
            # 갈 수 없으면 패스
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했다면, 패스
            if MST[next_node]:
                continue


            heapq.heappush(pq, (graph[node][next_node], next_node))

            # 이미 1을 방문함,
            # pq에는 남아있지만, 더 방문할 필요가 없더라!!!

        return min_weight





import heapq

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]


for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight



result = prim(0) # 출발 정점을 바꿔도 동일하다 (그리디 어쩌구라고 말씀)
print(f"최소비용은 {result}")