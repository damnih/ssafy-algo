import sys
sys.stdin = open("input.txt", "r")

# level 점원 수
# branch 탑에 포함 시킨다 / 안시킨다
def recur(cnt):
    global answer
    # 기저조건 가지키기
    # 이미 B이상인 경우라면 더 돌릴 필요 없지
    # 탑이 더 높아지는 경우는 필요 없음
    if total_height >= B:
        answer = min(answer, total_height)

    if cnt == N:
        return

    # 재귀를 시키는 대로 탑의 높이가 높아지거나 아니거나 되니깐
    recur(cnt + 1, total_height + heights[cnt]) # 탑에 포함 시키는 경우
    recur(cnt + 1, total_height) # 탑에 포함 안 시키는 경우

# 최소는 무조건 아무것도 선택 안한 케이스 ㅜㅜ 가 됨



T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = int(21e8) # 대충 큰 숫자가 필요할 때 이렇게 해주면 됨 21억 정도 나옴 ㅋㅅㅋ
    recur(0, 0)