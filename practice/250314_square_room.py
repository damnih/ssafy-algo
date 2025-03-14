import math
import sys
sys.stdin = open("input.txt", "r")

print(math.sqrt(8225)) # 90.69178573608527

# 정사각형 방 - 정답 코드
# 접근법
# - N*N visited 배열을 만든다
# 해당 숫자에서 갈 수 있다면 1을 기록한다
# 연속된 1의 길이가 가장 긴 곳이 정답이다
# 같은 길이가 있다면 작은 수가 정답 위치

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N ** 2 + 1)

    # 현재위치 숫자 기준 상하좌우 확인
    # 1 큰 곳이 있다면 visited 기록
    # # # 근데 여기서 1의 길이를 어케 재지? 그게 궁금하다
    # 델타 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(N):
        for c in range(N):
            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]

                # 델타이므로 벽 처리 필요함
                if not 0 <= new_c < N and 0 <= new_r <N:
                    continue
                if arr[new_r][new_c] == arr[r][c] + 1:
                    # 현재 숫자에서 다음 숫자로 이동이 가능하다면,
                    visited[arr[r][c]] = 1
                    break # 하나 찾았으니 나머지 방향은 볼 필요 없음
    # print(visited)
    # 이제 내가 궁금했던 거 나온다
    # 연속된 1의 개수가 가장 긴 곳을 찾는다!!!!!
    # 1. 가장 긴 곳, 2. 현재 몇 개인지, 3. 어디서부터 출발했는지 확인
    max_cnt = cnt = start = 0
    for i in range(1, N ** 2 + 1):
        if visited[i] == 1:
            cnt += 1
        else: # 1로 진행하다가 0을 만났을 때
            if max_cnt < cnt: # 앞의 숫자부터 봐줘야 하기 때문에 = 안쓰는게 맞음 앞서있을수록 유지
                max_cnt = cnt
                start = i - cnt # 시작점을 찾아줘야 하는 거니깐 !
            cnt = 0 # 개수 세는 카운트 다시 초기화 ㅇㅇ # 담 셀 때는 바로 해줘야 하니깐
    print(f"#{tc} {start} {max_cnt + 1}")


