
# import sys
# sys.stdin = ("1953_sample_input.txt", "r")

from pprint import pprint 

# BFS 문제임 
# BFS는 큐에 넣을 때 방문처리해주는거징~~ 


# 위치에 갔을때, 상하좌우 델타 탐색을 하고 
# 탐색을 한 그 새로운 곳이 과연 갈 수 있는 곳인지에 대해서 생각해봐야함 

# 아 아직 기억이 넘 생생하게 살아있다 
# 나는 이 문제를 첨 보고 
# 결국 이건 큐에 넣을 때 갈수있는지 여부를 
# 어떻게 가리느냐가 핵심이 될 거라고 걱정했단말임
# 어케해야지 하고,, 진짜 예전에 했던 것처럼 
# 노가다로 다 경우의 수 나눠서 이프문 7개 돌려야하나 하고,, 
# 근데 딕셔너리로 만들어서 조회하는 식으로,, 만드셨더라 ㅎ 
# 아직 이 기억이 너무 생생해 
# 걍 이 기억을,, 따라가자 ㅎㅎ 



pipe_dict = {
    0: [0, 0, 0, 0],
    1: [1, 2, 3, 4],
    2: [1, 2, 0, 0],
    3: [0, 0, 3, 4],
    4: [1, 0, 0, 4],
    5: [0, 2, 0, 4],
    6: [0, 2, 3, 0],
    7: [1, 0, 3, 0]
}

# 그니깐 이렇게 연결했으니까 
# 지금 나의 번호로 여길 조회해서 상 하 좌 우 의 탐색을 유지하면 되,, 는 ,, 거얌 ㅎㅎ
# 그담에 내가 갈 수 있는 곳에 있는 녀석이 연결되는 곳인지 확인하면 되겠지? 
# 이게 다행히도 상하좌우 얘기라서 이전거랑 한칸씩만 옮겨서 비교하면 되겠당 야호 

# 아 내가 기억하다 말았네 이렇게 조회할거면 
# 솔직히 걍 델타탐색을 해서 상하좌우를 볼 필요가 없지 않나? 
# 걍 바로 파이프 조회만 하면 되네 
# 대신 저기에 0도 넣어주장 
# 아니야 필요해 저 인덱스로 조회해서 상하좌우 가줄거라서 ㅇㅇㅇㅇㅇㅇㅇ 

T = int(input())
for tc in range(1, T+1):
    
    N, M, R, C, L = map(int, input().split())
    
    manhole = [list(map(int, input().split())) for _ in range (N)]
    
    visited = [[0] * M for _ in range(N)]

    visited[R][C] = 1

    # 탐색 순서가 어떻게 될까
    # 일단, 맨홀을 타고 내려간 그 좌표의 파이프 정보를 조회해 
    # 그래서 거기에서 갈 수 있는 녀석들의 위치를 알아봐
    # 갈 수 있는 녀석들의 정보를 조회해서 입구 뚫려있는지 그 정보를 조회해
    # 근데 이 입구 뚫려있는거 처리를 어케해야할까,, 
    # 일단 하면서 생각해보자 솔직히 상하.좌우 묶여있으니깐 한칸씩이긴한데 
    # 02일때 13일때 일케 나눠서 생각하면 될려나 
    # 그래서 갈 수 있다면, 큐에 넣어주면서~! 그것을해준다 무엇? 방문처리 

    q = [(R, C)] # 그냥 넣은채로 시작해도 ㄱㅊㄱㅊ 

    while q:
        cur_node = q.pop(0) # BFS는 선입선출의 큐! 
        cur_i = cur_node[0]
        cur_j = cur_node[1]

        # 이 현재 뽑아낸 좌표에 대해, 맨홀의 타입을 확인해야해
        manhole_type = manhole[cur_i][cur_j]
        # 이 타입의 맨홀이 갈 수 있는 위치를 조회해보자
        manhole_type_list = pipe_dict[manhole_type] # 이건 리스트임
        # 이제 순회를 돌면서,, 음,, 이거 근데 그냥,, 조회 안하고 바로 요소를 뽑아내서 봐도 ㄱㅊ을듯?
        for dir_info in manhole_type_list:
            # 그냥 무식하게 4방향 모든 케이스를 경우의 수를 나눠서 지정해주자 
            if dir_info == 0:
                continue
            elif dir_info == 1: # 상으로 갈 수 있는거임
                next_i = cur_i - 1
                next_j = cur_j
                # 그렇다면 이 넥좌표에 대해 벽처리 해주고
                if 0 <= next_i < N and 0 <= next_j < M:
                    # 벽 안에 있다면 이 넥좌표가 어떤 방향으로 갈 수 있는지 확인을 해줌
                    # 난 지금 위로 가는 것만 생각하고 있으니깐 이 넥좌표는 아래에서 받아줄 수 있는지 여부가 중요
                    # 넥좌표 딕셔너리에 하가 있다면,
                    next_manhole_type = manhole[next_i][next_j]
                    if pipe_dict[next_manhole_type][1] == 2:
                        # 있다면, 갈 수 있는 거니깐 큐에 넣어주고 방문처리 해주자
                        # 방문처리 하기 전에 갔던 곳인지 확인하고 안간곳에 한해서 가줘야해
                        if visited[next_i][next_j] == 0:
                            visited[next_i][next_j] = visited[cur_i][cur_j] + 1
                            next_node = (next_i, next_j)
                            q.append(next_node)
                            # pprint(visited)

            elif dir_info == 2: # 하로 갈 수 있는거임
                next_i = cur_i + 1
                next_j = cur_j
                # 그렇다면 이 넥좌표에 대해 벽처리 해주고
                if 0 <= next_i < N and 0 <= next_j < M:
                    # 벽 안에 있다면 이 넥좌표가 어떤 방향으로 갈 수 있는지 확인을 해줌
                    # 난 지금 아래로 가는 것만 생각하고 있으니깐 이 넥좌표는 위에서 받아줄 수 있는지 여부가 중요
                    # 넥좌표 딕셔너리에 상이 있다면,
                    next_manhole_type = manhole[next_i][next_j]
                    if pipe_dict[next_manhole_type][0] == 1:
                        # 있다면, 갈 수 있는 거니깐 큐에 넣어주고 방문처리 해주자
                        # 방문처리 하기 전에 갔던 곳인지 확인하고 안간곳에 한해서 가줘야해
                        if visited[next_i][next_j] == 0:
                            visited[next_i][next_j] = visited[cur_i][cur_j] + 1
                            next_node = (next_i, next_j)
                            q.append(next_node)
                            # pprint(visited)

            elif dir_info == 3: # 좌로 갈 수 있는거임
                next_i = cur_i
                next_j = cur_j - 1
                # 그렇다면 이 넥좌표에 대해 벽처리 해주고
                if 0 <= next_i < N and 0 <= next_j < M:
                    # 벽 안에 있다면 이 넥좌표가 어떤 방향으로 갈 수 있는지 확인을 해줌
                    # 난 지금 좌로 가는 것만 생각하고 있으니깐 이 넥좌표는 우에서 받아줄 수 있는지 여부가 중요
                    # 넥좌표 딕셔너리에 우가 있다면,
                    next_manhole_type = manhole[next_i][next_j]
                    if pipe_dict[next_manhole_type][3] == 4:
                        # 있다면, 갈 수 있는 거니깐 큐에 넣어주고 방문처리 해주자
                        # 방문처리 하기 전에 갔던 곳인지 확인하고 안간곳에 한해서 가줘야해
                        if visited[next_i][next_j] == 0:
                            visited[next_i][next_j] = visited[cur_i][cur_j] + 1
                            next_node = (next_i, next_j)
                            q.append(next_node)
                            # pprint(visited)

            elif dir_info == 4: # 우로 갈 수 있는거임
                next_i = cur_i
                next_j = cur_j + 1
                # 그렇다면 이 넥좌표에 대해 벽처리 해주고
                if 0 <= next_i < N and 0 <= next_j < M:
                    # 벽 안에 있다면 이 넥좌표가 어떤 방향으로 갈 수 있는지 확인을 해줌
                    # 난 지금 우로 가는 것만 생각하고 있으니깐 이 넥좌표는 좌에서 받아줄 수 있는지 여부가 중요
                    # 넥좌표 딕셔너리에 좌가 있다면,
                    next_manhole_type = manhole[next_i][next_j]
                    if pipe_dict[next_manhole_type][2] == 3:
                        # 있다면, 갈 수 있는 거니깐 큐에 넣어주고 방문처리 해주자
                        # 방문처리 하기 전에 갔던 곳인지 확인하고 안간곳에 한해서 가줘야해
                        if visited[next_i][next_j] == 0:
                            visited[next_i][next_j] = visited[cur_i][cur_j] + 1
                            next_node = (next_i, next_j)
                            q.append(next_node)
                            # pprint(visited)

    # pprint(visited) # 엉 만족스럽게 나온다 
    # 그러면 이렇게 만들어낸 visited를 활용해 
    # 값이 L 이하인 요소들의 개수를 검출해 내면 돼 ^^! 

    count = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                count += 1

    print(f'#{tc} {count}')



