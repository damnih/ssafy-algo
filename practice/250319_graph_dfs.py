import sys
sys.stdin = open("lecture_input.txt", "r")

N, M = map(int, input().split())




def dfs(node):
    # 보통 그래프 문제에서
    # K개의 노드 방문했다면 종료
    # N개를 모두 방문했다면 경로 출력
    # if 종료 시 해야할 것들 or
    # 종료조건 여기서 해주는거임

    print(node, end=" ")
    # visited[node] = 1 # 문제마다, 개발자마다, 이 시작점 초기화해주는 구현 방식이 다름
    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라!
        # 이거 때문에 딱히 종료조건이 존재하지 않아도 언젠간 종료됨
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향이라면 여기서도 이렇게 뒤집어서 받아줘야함

visited = [0] * (N + 1) # 방문 여부 기록

# 출발점 초기화를 하는 방법은 문제마다 개발자마다 다르다
# 강사님은 여기서 dfs를 시작하기 전에 바로 방문을 처리해주고, dfs를 찍을 것임
visited[1] = 1

dfs(1)
