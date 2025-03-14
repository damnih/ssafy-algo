# 람다 연습을 할 겸
# 그냥 정렬해서 해 봅시다아아아아~!

'''

3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N = 10
    # N = 8

    timetable = [list(map(int, input().split())) for _ in range(N)]
    # timetable = [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]
    # timetable = [[14, 23], [2, 19], [1, 22], [12, 24], [21, 23], [6, 15], [20, 24], [1, 4], [6, 15], [15, 16]]
    # timetable = [[2, 9], [1, 9], [6, 8], [5, 10], [1, 2], [4, 5], [1, 3], [2, 5]]


    # print(timetable)

    # 이 타임테이블을 정렬해준다 = sort
    # 어떤 기준으로? 키 값을 기준으로!
    # 그 키는 어떤 키일까,, 바로바로 끝나는 곳이야
    # 그니깐 키 기준이 바로 이 람다 함수가 되는거고 이 함수는 바로 두번째인자가 되는거지 ㅇㅇㅇㅇㅇㅇ
    # 이러면 되는걸까??
    # timetable.sort(key = lambda x : x[1])
    # [[1, 2], [1, 3], [4, 5], [2, 5], [6, 8], [2, 9], [1, 9], [5, 10]]
    timetable.sort(key = lambda x : (x[1], x[0]))
    # [[1, 2], [1, 3], [2, 5], [4, 5], [6, 8], [1, 9], [2, 9], [5, 10]]
    # print(timetable)
    # 잘된다 잘된다 야호

    # 그렇다면 이제 이걸 이용해서 끝나는 값이 가장 작은 순으로 먼저 조회해주자

    # 조회 했으니깐 이 timetable에 대해서~~
    # 일단 앞에서부터 돌면 도착시간이 빠른 순이잖아 그러니 걔로 먼저 순회해주고,시작시간으로 커트해주면 되겠지


    # 그니깐 이거는 한번 지나간 버스시간표에 대해서는 더 보지 않을거잖아
    now_e = timetable[0][1] # 이게 처음으로 나오는 시간표의 도착시간,
    cnt = 1 # 시작은 무조건 한번 먹었으니깐 ㄱㅊ아!!
    for time in timetable: # 이렇게 하면 이 정렬한 애들 기준으로 순서대로 나와주겠지?
        next_s = time[0]
        next_e = time[1]
        if now_e <= next_s: # 현재 끝점보다 다음 시작점이 늦다면, 갈수있는거지 !
            now_e = next_e
            # 그리고 탈 수 있는 거니깐 카운트 올려놔야함
            cnt += 1

    print(f"#{tc} {cnt}")








# for i in range(N):
#     for j in range(i, N): # 도착시간 이후로 봐줘야하지~~~
#         # 만약 다음 배차의 시작시간이 이전 배차의 도착시간보다 같거나 늦다면,
#         if timetable[j][0] >= timetable[i][1]:

# 아냐 이건 반복을 하기가 어렵잖아
# 그냥 while로 넣어주자

# 나 그냥 재귀해볼래
# def timetable_setting(timetable, start, end):
#     # 시작시간과 끝시간을 넣어주면 될거같은데?
#     # 일단 종료조건을 생각해보자 무엇이 종료 조건이냐면,,
#     # 더 넣어줄 인자가 없을 때다!!!
#     # 음 이거 종료조건 잡기 어렵기는 하네
#     # 1. 일단 내 끝나는 시간 이후로 시작하는 타임이 없는 경우
#     # 2. 내 끝나는 시간 이후로 시작하지만 끝나는 시간이 24시 이후일 경우
#     # 그니깐 이 두 조건의 반대를 동시에 만족한다면 계속 재귀가 돌아
#     if timetable[i+1][0] > timetable[i][1] and timetable[i+1][1] <= 24:
#
# timetable[i][0] # i번째 배치의 시작점
# timetable[i][1] # i번째 배치의 끝점
#
# now_s = timetable[][0]
# now_e
# next_s
# next_e




