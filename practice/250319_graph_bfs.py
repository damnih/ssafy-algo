import sys
sys.stdin = open("250319_lecture_input.txt", "r")


def bfs(start_node):
    # q에 들어가는 노드들의 의미: 다음에 방문해야 할 노드들
    q = [start_node] # 시작점을 넣은 상태로 출발

    while q: # 대기열이 빌 때까지 계속 하는거임


    # 1. 가장 앞에 있는 노드를 뽑는다
    # 2. 해당 노드에서 갈 수 있는 노드들을 q에 넣는다
        now = q.pop(0)

        print(now, end=" ")

        # 인접한 노드들을 확인하면서
        for next_node in graph[now]:
            # 방문했으면 pass
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)

            # 여기서 재귀를 쓸 일은 없는거임





N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)

