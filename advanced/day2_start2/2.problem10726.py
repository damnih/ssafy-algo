import sys
sys.stdin = open("input.txt", "r")

# M의 우측 N개를 확인 (반복문을 활용한 방법)
# - 하나라도 0이 나오면 False
# def solution():
#     target = M
#     # N 번 확인한다.
#     for _ in range(N):
#         # 맨 우측 비트가 1인 지 체크
#         # 0x1, 0b1, 1 다 사용 가능
#         # - 0x1: 비트 연산이라는 것을 명시하기 위해 사용
#         if target & 0x1 == 0:
#             return False
#         # 맨 우측 비트를 삭제
#         target = target >> 1
#     return True


# 업그레이드 버전
def solution():
    # N 개의 1 을 구함
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()