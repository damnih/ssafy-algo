# 그냥 DFS 돌려서 경로 합을 구하자 ㅋ
from pprint import pprint


# 어차피 직전 경로는 둘 중 하나임
# 최소합이라는건 결국 둘 중 하나에서 작은 것들만 계속 선택해나가면 자연스럽게 만들어지는거임
# 즉 가능한 직전 경로를 기억해뒀다가 조회해서 더해나가는 식으로 미리 sum해둔 값을 만들어두면 좋겠당

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 첫줄만 어케 만들어서 기억을 해주자 그러면 나머지는 기억한거 조회해서 채워넣을 수 있는거잖아?
    # matrix = []
    sum_mat = [[0]*N for _ in range(N)]

    sum_mat[0][0] = matrix[0][0]

    for i in range(1, N):
        sum_mat[i][0] = matrix[i][0] + sum_mat[i-1][0]

    for j in range(1, N):
        sum_mat[0][j] = matrix[0][j] + sum_mat[0][j-1]
    # print(sum_mat)

    for cur_r in range(1, N):
        for cur_c in range(1, N):
            sum_mat[cur_r][cur_c] = matrix[cur_r][cur_c] + min(sum_mat[cur_r - 1][cur_c], sum_mat[cur_r][cur_c -1])
            # 이렇게 된다는 거잖아;

    # print(sum_mat)
    # 어 완벽하네,,

    # 그렇다면 답은 항상 그거네
    ans = sum_mat[N-1][N-1]

    print(f"#{tc} {ans}")



'''
완성본 



N = int(input())
# N = 4
matrix = [list(map(int, input().split())) for _ in range(N)]
# matrix = [
#     [2, 4, 1, 3],
#     [1, 1, 7, 1],
#     [9, 1, 7, 10],
#     [5, 7, 2, 4]]
# pprint(matrix)

# 이거 그냥 우우하하, 두개의 모든 순열을,, 중복없이 구해주면,, 되는거아냐?
# 우우하하
# 우하우하
# 우하하우
# 하우우하
# 하하우우
# 하우하우
# 이 6개의 조건,,
# 우 N-1개
# 하 N-1개
# 얘네를 중복없이 순열 ㄱㄱ



# 내가 해주고 싶은 것이 무엇이냐?

# 우우 하하 이거 에바임 버려 



# 첫줄만 어케 만들어서 기억을 해주자 그러면 나머지는 기억한거 조회해서 채워넣을 수 있는거잖아? 
# matrix = []
sum_mat = [[0]*N for _ in range(N)]

sum_mat[0][0] = matrix[0][0]

for i in range(1, N):
    sum_mat[i][0] = matrix[i][0] + sum_mat[i-1][0]

for j in range(1, N):
    sum_mat[0][j] = matrix[0][j] + sum_mat[0][j-1]

# print(sum_mat)


for cur_r in range(1, N):
    for cur_c in range(1, N):
        sum_mat[cur_r][cur_c] = matrix[cur_r][cur_c] + min(sum_mat[cur_r - 1][cur_c], sum_mat[cur_r][cur_c -1])
        # 이렇게 된다는 거잖아;

# print(sum_mat)
# 
# 어 완벽하네,,

# 그렇다면 답은 항상 그거네 
ans = sum_mat[N-1][N-1]

print(f"#{tc} {ans}")


'''



'''
dr = [0, 1]
dc = [1, 0]

start_r, start_c = 0, 0
start = start_r, start_c
cur_r, cur_c = start_r, start_c
is_final = False
stack = [start]
trace = [matrix[start_r][start_c]]
while is_final == False:
    if stack:
        cur_r, cur_c = stack.pop()
        if (cur_r, cur_c) == (4, 4):
            is_final = True
        # 만약 도착점에 온 게 아니라면,
        # 나는 지금 이 현재 위치에 대해서,, 뭘해줘?
        # 방문처리, 벽 그런거 다 필요 없어,
        # 그냥 순수하게 나 갔으니깐 족적 남겨 ㅇㅇ
        trace.append(matrix[cur_r][cur_c])
        # 그 다음에 할 일은? 다음 위치 탐색하는 거다
        for dir in range(2): # 아래 혹은 오른쪽
            next_r = cur_r + dr[dir]
            next_c = cur_c + dc[dir]
            # 이 탐색한 다음 좌표에 대해
            if 0 <= next_r < N and 0 <= next_c < N: # 벽 안에 있는지 확인해주고, 갈수있다면,
                # 얘는 경우의 수 가지가 뻗어나가면서 한 군데 탐색이 끝나면 바로 직전 경로에서 탐색하잖아
                # 후입선출이니까 스택이네?
                # matrix[next_r][next_c]
                next = next_r, next_c
                stack.append(next)
                # print(stack)
            if next_r == N-1 and next_c == N-1:
                is_final =True
                print(trace)
    else:
        is_final = True
# 근데 얘는 모든 경우의 수를 보는게 아니야 ㅜ
#
# 걍 우하 우하 우하 둘 중 하나의 경우의 수를 가지고 가지치기를 해가며
# 위치를 넣어줘야 하나?
'''


# stack = [start]
# trace = []
#
# visited = [[0] * N for _ in range(N)]
#
# while stack:
#     cur_node = stack.pop()
#     cur_r = cur_node[0]
#     cur_c = cur_node[1]
#     if visited[cur_r][cur_c] != 1: # 근데 이게 필요할까? 어차피 안 간 곳으로만 갈텐데
#         visited[cur_r][cur_c] = 1
#         trace.append(matrix[cur_r][cur_c])
#         for dir in range(2):
#             next_r = cur_r + dr[dir]
#             next_c = cur_c + dc[dir]
#             if 0 <= next_r < N and 0 <= next_c < N:
#                 next = next_r, next_c
#                 stack.append(next)

# print(trace)