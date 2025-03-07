# # 파리 퇴치
# ## 데이터를 input한것을 받아준다.
# import sys
# sys.stdin = open('input.txt')
# def kill_fly(N, M, arr):
#     summation_list = []
#     for row in range(N-M+1):
#         for col in range(N-M+1):
#             summation = 0
#             # 순행탐색을 수행하면서 그값을 position에 할당한다.
#             # 델타 탐색을 할건데 파리채의 크기는 M*M이다.
#             for k in range(M):
#                 for l in range(M):
#                     summation += arr[row+k][col+l]
#
#             summation_list.append(summation)
#
#     return max(summation_list)
#
# T = int(input())
# for test_case in range(1,T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     print(f"#{test_case} {kill_fly(N, M, arr)}")

