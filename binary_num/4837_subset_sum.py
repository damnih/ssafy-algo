# N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
#
# 해당하는 부분집합이 없을 경우 0
# 모든 부분집합을 만들어 답을 찾아도 ㄱㅊ
#
# 근데 나는 그냥 개수 N개인 부분집합만,, 만들래 ㅎㅎ
# # 이게 더 어려울 거 같다,,
# 그냥 부분집합을 전부 구하고, 거기서 len 3인 애들 거르고 거기서 합을 고르자 ㅇㅇ

# 1부터 12까지의 숫자를 원소로 가짐 ㅇㅇ 중복 없어 ㅎㅎ 원소 12개야 ㅎㅎ

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

full_subset = []

subset_num = 2 ** len(A)

for i in range(subset_num):
    # 이 i는 01로 조회해서 부분집합의 그걸 넣어줄 놈임
    subset = []
    for j in range(len(A)):
        # 이 j는 왼쪽으로 밀면서 0인지 1인지 조회하는 그거임
        if i & (1 << j): # 비트연산으로 1이 있는지 확인
            subset.append(A[j])
    # 이 뽑아낸 부분집합을 전체 부분집합에 넣어줘야할듯 !!
    full_subset.append(subset)

# print(full_subset)

# full_subset은 두고두고 쓸거니깐 걍 for문 밖에 빼두자

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    N_subsets = []

    for subset in full_subset:
        if len(subset) == N:
            N_subsets.append(subset)

    # print(N_subsets)

    ans_list = []
    for N_sub in N_subsets:
        if sum(N_sub) == K:
            ans_list.append(N_sub)

    ans = len(ans_list)
    print(f"#{tc} {ans}")