# print(7 >> 1) # 3

# print(bin(5)) # 0b101
# print(bin(-5)) # -0b101


# 스웨아 10726
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS
# 하나라도 0이라먄 끗 

# 정수 N, M이 주어질 때 M의 이ㅣㄴ수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지 


# M의 우측 N개를 확인할 예정 
# def solution():
#     target = M
#     for i in range(N):
#         # if target & 1 == 0: 
#         #   return False
#         #     # 요거는 될까 안될까 
#         #     # 이렇게 쓰면 for i 가 아니라 _로 써줘야함
#         #     # 가능하대 
#         #     # 맨 오른쪽 것만 1인지 체크하는 개념이 되는 거임 
#         #     # 맨 우측 비트를 삭제하는 거
#         # # 0x1: 비트 연산이라는 것을 명시하기 위해 사용
#         if target & 0x1 == 0:
#             return False 
#         target = target >> 1


# 단순하게 하는 방법
# N개의연속된 비트가 확인하는거니깐 
# N의 자리를 다 돌면 되는거잖아 

# 비트마스킹 기법임
# N개의 1을 구하는거

def solution():
    # N개의 1을 구함 
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result 


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())


