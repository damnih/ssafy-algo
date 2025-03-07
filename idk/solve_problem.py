# def electric_bus(K,N,M,arr):
#     '''
#     :param K: 한번에 최대 이동 가능한 정류장 수
#     :param N: 전체 정류장 개수
#     :param M: 충전기가 설치된 정류장 개수
#     :param arr: 충전기가 설치된 정류장 인덱스
#     :return:
#     '''
#     idx = 0
#     conclusion_list = []
#     while idx < N:
#         # arr을 순회하면서 값을 봐야함.
#         # 만약 정류장 간에 간격이 K보다 크다면 0을 반환
#         for station in range(M-1):
#             if arr[station+1] - arr[station] > K:
#                 return 0
#
#         # idx+K값이 10을 넘는지 확인하고
#         for j in range(M - 1, -1, -1):
#             if idx + K >= N:
#                 return len(conclusion_list)
#             ## 만약 arr[j]
#             elif idx + K >= arr[j]:
#                 idx = arr[j]
#                 conclusion_list.append(idx)
#                 break
#
#
#
#
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     print(f"#{test_case} {electric_bus(K,N,M,arr)}")


# # light_switch랑 charlie_puth
# def light_switch(switch_count, switch_condition, T, arr):
#     ## 처음 들어온 array에 값을 확인한다.
#     for i in range(T):
#         human, number = int(arr[i][0]), int(arr[i][1])
#         ## 만약 남자면
#         if human == 1:
#             ## 받은숫자의 배수에 해당하는 스위치 값 바꾼다
#             for j in range(1, (switch_count // number) + 1):
#                 # 만약 switch condition에 해당하는 값의 배수가 1이면 0넣고
#                 if switch_condition[number * j - 1] == 1:
#                     switch_condition[number * j - 1] = 0
#                 # 만약 switch condition에 해당하는 값의 배수가 0이면 1넣는다.
#                 elif switch_condition[number * j - 1] == 0:
#                     switch_condition[number * j - 1] = 1
#
#
#         # 만약 여자면
#         elif human == 2:
#             ## 자기가 받은 수 기준으로 좌우가 대칭이면 스위치를 바꾼다.
#             for k in range(switch_count // 2):
#                 # 만약 내가 받은 왼쪽 수와 오른쪽 수가 같으면
#                 if switch_condition[number - 1 - k] == switch_condition[number - 1 + k]:
#                     if switch_condition[number - 1 - k] == 1:
#                         switch_condition[number - 1 - k], switch_condition[number - 1 + k] = 0,0
#                     elif switch_condition[number - 1 - k] == 0:
#                         switch_condition[number - 1 - k], switch_condition[number - 1 + k] = 1,1
#
#
#     return switch_condition
#
#
# switch_count = int(input())
# switch_condition = list(map(int, input().split()))
# T = int(input())
#
# arr = [list(map(int, input().split())) for _ in range(T)]
# print(arr)
# print(light_switch(switch_count, switch_condition, T, arr))

# '''
# 8
# 0 1 0 1 0 0 0 1
# 1
# 1 3
# '''
#
#
# def light_switch(switch_count, switch_condition, number_of_student, member):
#     for i in range(number_of_student):
#         human, number = member[i][0], member[i][1]
#
#     # 만약 남자 학생이 들어온 경우
#     if human == 1:
#         # 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치 상태변환
#         for j in range(1, switch_count//number+1):
#             if switch_condition[j*number-1] == 1:
#                 switch_condition[j * number - 1] = 0
#             elif switch_condition[j*number-1] == 0:
#                 switch_condition[j * number - 1] = 1
#
#
#     # 만약 여자 학생이 들어온 경우
#     elif human == 2:
#         #  자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
#         for k in range(min(number, switch_count-number+1)):
#             if switch_condition[number - 1 - k] == switch_condition[number-1+k]:
#                 # 만약 switch_condition이 같으면 1인지 0인지 확인하고 바꾼다.
#                 if switch_condition[number - 1 - k] == 1:
#                     switch_condition[number - 1 - k] = 0
#                     switch_condition[number - 1 + k] = 0
#                 elif switch_condition[number - 1 - k] == 0:
#                     switch_condition[number - 1 - k] = 1
#                     switch_condition[number - 1 + k] = 1
#             elif switch_condition[number - 1 - k] != switch_condition[number - 1 + k]:
#                 break
#
#     result = ' '.join(map(str, switch_condition))
# # 20개씩 출력
#     for i in range(0, switch_count, 20):
#         print(' '.join(result.split()[i:i + 20]))  # 20개씩 출력
# switch_count = int(input())
# switch_condition = list(map(int, input().split()))
# number_of_student = int(input())
# member = [list(map(int, input().split())) for _ in range(number_of_student)]
# light_switch(switch_count, switch_condition, number_of_student, member)










































































