def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    rootx = find_set(x)
    rooty = find_set(y)

    if rootx == rooty: # 사이클 방지 # 이미 같은 집합에 속해있으면 연결하지 말아라 이런 의미임
        return
    # 일정한 규칙으로 연결하자! 라는 룰에 의해 조건을 조금씩 설정하는거임
    # 그래서 나는 더 작은 쪽으로 연결해주자 이런 룰을 추가한거임
    if rootx < rooty:
        parent[rooty] = rootx

    if rooty < rootx:
        parent[rootx] = rooty

edges.sort(key=lambda x: x[2]) # 가중치 기준으로 정렬/
parent = [i for i in range(V + 1)]


# 언제까지? N-1개를 선택할 때까지
cnt = 0
result = 0 # MST 가중치의 합

for u, v, w in edges:
    # u와 v가 연결이 안되어있으면 선택
    #
    if find_set(u) != find_set(v):
        print(u, v, w)
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1: # MST 구성이 끝났다.
            break

print(result)