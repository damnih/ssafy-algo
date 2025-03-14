import sys
sys.stdin = open("1861_input.txt", "r")


# 상하좌우에 붙은 방 중 나보다 1 큰 방으로만 이동할 수 있음

# 이런 경우엔 2차원 배열이잖아
# 1차원 배열로 생각해서 가능 불가능 여부를 기억하는 식으로 만들어주는게 좋다 데이터 정리에 좋다!

# 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와
# 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.

# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


# 일단 배열을 받아야겠징

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room_matrix = [list(map(int, input().split())) for _ in range(N)]

    # 일단 1부터 N^2까지의 수를 순회하며, 얘가 갈 수 있는지 여부를 탐색
    can_go = [0] * (N ** 2 + 1)
    # 근데 이건 사실상 델타탐색이잖아~!

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            # 이 현재 좌표에 대해,,
            now = room_matrix[r][c] # 현재 좌표의 값
            for dir in range(4):
                next_r = r + dr[dir]
                next_c = c + dc[dir]
                # 벽처리
                # 방법 1
                # if 0 <= next_r < N and 0 <= next_c < N:
                #     next = room_matrix[next_r][next_c]
                #     # 이 넥스트 좌표 중에 지금 내 값보다 +1이 있다면,
                #     if next == now + 1:
                #         can_go[now] = 1
                #         break # 찾는 순간 더 돌 필요 없잖아 ㅋㅋ
                # 방법 2
                if 0 <= next_r < N and 0 <= next_c < N and room_matrix[next_r][next_c] == now + 1:
                    can_go[now] = 1
                    break
                # 둘 다 되넹

    # print(can_go)
    # 이제 나오는 can_go가 바로 이동할 수 있는지 여부를 확인할 수 있는 cango인거임

    # 그럼 이제 이 나온 can_go에 대해서,,
    # 1이 얼마나 연속적으로 있는지 확인할거임
    # 이건 결국 인덱스를 넘어가면서,, 내가 1이면 카운트 +1 0이면 카운트 멈춰주면 되는거잖아??
    #
    # 그리고 나는 그 때의 인덱스도 필요함 시작 인덱스,,
    #
    # 고로 일단 start와 cnt를 만들어주면 되겠다

    start = 0
    cnt = 0
    max_cnt = 0

    # 이 배열의 길이만큼만 돌아줄 거니깐 끝이 정해져있어 ㅇㅇ for문이다
    for i in range(1, N ** 2 + 1):
        if can_go[i] == 1:
            cnt += 1
        else: # 0일 경우
            # 카운트 더해주는거 멈추고,
            # 이 때의 카운트가 맥스 카운트인지 비교해서 갱신해주고, 이 때의 시작점 찾아주면 됨
            if cnt > max_cnt: # 왜 같은 경우는 빼주냐면 같을 경우에는 걍 앞의 인덱스 반환할거라 그럼
                max_cnt = cnt
                start = i - cnt
            # 이 조건이 아니더라도 0으로 초기화는 해줘야하니깐 if문 밖에 있어야한다
            cnt = 0

    print(f"#{tc} {start} {max_cnt + 1}")