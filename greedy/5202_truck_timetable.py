# 최대 몇 대의 화물차가 이용 가능한지
# 회의실 문제다.. 

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


# T = int(input())
N = int(input())

# for _ in range(N):
#     s, e = map(int, input().split())
timetable = [list(map(int, input().split())) for _ in range(N)]

print(timetable)

# 그렇다면 도착 시간 기준으로 오름차순 해주고 싶은데!!!!!! 어케하면 될까 
# 자리를 바꿔주는 법밖에 몰라 나는,, 

# 어 잠만 
# 이 로직은 생각해보면 남은 시간 내에서, 젤 빨리 끝나는 애 기준으로 델고오는 거잖아? 
# 남 은 시 간
# 이게 중요하다 
# 남 은 시 간 
# 그렇다면, 사용 가능한 시간의 start와 end를 정해두고 
# 이걸 바꿔가면서 이 범위 내에서 탐색을 해주면 되지 .. 않을까?? 

start = 0 
end = 24 
cnt = 0


while start < end:
    min_end = timetable[0][1]
    cnt += 1
    # min_end 를 만들어서 얘를 계속 교환해주자!!! 
    for i in range(N):
        # 근데 일단 이거는 이 녀석의 시작점이 직전의 엔드보다 크거나 같아야 하잖아
        # 가용시간 내여야 하잖아 
        if start <= timetable[i][0]:
            # 만약 탐테에서 꺼낸 엔드가 지금 지정한 최솟값보다 작다면, 
            if timetable[i][1] < min_end:
                # 최소 도착 시간을 지정해줌 
                min_end = timetable[i][1]
    # 이 포문이 끝나면, 정해진 min_end가 생기겠지? 
    # 이게 새로운 start가 되는 거임
    start = min_end
    

    # 이거를 계속 반복하는거임 언제까지? 
    # 이 min_end가 end보다 커질 때까지 ㅇㅇ 

print(cnt)

