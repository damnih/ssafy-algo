# 4*4 n queen 문제
# y, x 좌표에 queen 을 놓은 적이 있다
# visited 기록 방법
# 1. 이차원 배열
# 2. 일차원 배열로 효율저그로 하는 방법
#
# 재귀함수는 항상
# level
# branch
# 가 중요함

# level: 재귀가 언제까지 돌아야 할까,,
#        n개의 행에 모두 놓았다면, 성공
# branch: N개의 열
def check(row, col):
    # 현재 같은 열에 놓은 적 있는지 확인
    # 대각선에 놓은 적 있는지 확인
    # 같은 열 확인
    for i in range(row):
        # if visited[i][col] == 1:
        if visited[i][col]: # 어차피 트루펄스 반환으로 할테니깐
            return False
    # 왼대각선 확인

    # 오른대각선 확인


def dfs():
    global answer
    if row == N: # 모두 놓으면 성공한 케이스
        answer += 1
        return

    # 가지치기를 하지 않고 모든 케이스를 다 둬볼겡
    for col in range(N):
        if chech(row, col) is False:
            continue

        visited[row][col] = 1

        dfs(row + 1)


    pass