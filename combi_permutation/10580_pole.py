import sys 
sys.stdin = ("10580_input.txt", "r")

# 교차점이 생기는 경우는 두 개의 직선이 만날때 ^^ 
# 두 직선만 뽑아서 교점이 있는지 없는지 여부만 생각하면 됨 ㅇㅇ 

T = int(input())
for tc in range(1, T+1):
    # 직선 1의 시작점, 끝점 
    # 직선 2의 시작점, 끝점 

    # 전선의 개수 N 이 주어짐 
    N = int(input())
    # 전선의 시작점과 끝점 ㅇㅇ 
    # 전선의 시작점&끝점의 정보 
    pole = [list(map(int, input().split())) for _ in range (N)]

    # start = pole[전선넘버][0]
    # end = pole[전선넘버][1]

    # 그렇다면 이 전선넘버를 안섞이게 그냥 고를수있으면 좋을텐데,, nC2 ㅋㅋㅋ 
    # 걍 내 넘버보다 한칸 뒤에서부터 시작해가면 되겠다 

    # 아 이거 뭐 시간 생각해야 하는데,, 근데 이거 머,, 이중포문이니깐 N^2 일거같은디
    # 시간을 어케 생각하라그랬지 
    # 근데 N의 최댓값이 1000개네 이중포문 돌면 1,000,000개네 
    # 시간 얼마인거임? 몰,, 르겟다,,,,, 

    cross_point = 0

    for i in range(N):
        for j in range(i, N):
            start_1 = pole[i][0]
            end_1 = pole[i][1]
            start_2 = pole[j][0]
            end_2 = pole[j][1]
            
            # 첫번째 전선이 좌상 우하 / 두번째 전선이 좌하 우상일 경우 
            if start_1 > start_2 and end_1 < end_2:
                cross_point += 1
            
            # 첫번째 전선이 좌하 우상 / 두번째 전선이 좌상 우하일 경우 
            elif start_1 < start_2 and end_1 > end_2:
                cross_point += 1 
            
            # 이 값들 이외에 딱히 고려할 건 없음, 왜냐하면,, 걍,, 이 조건에 대해서만 생각을 해줬기 때문에,, 
            # 그니깐 걍 전부 else로 빼줘서 pass하면 포문 정상적으로 돌고 ㄱㅊ을듯 
            else:
                continue
            # 아 함수가 아니라 그냥 반복문이니깐 컨티뉴다 

    # print(cross_point) # 잘됨 
    print(f"#{tc} {cross_point}")