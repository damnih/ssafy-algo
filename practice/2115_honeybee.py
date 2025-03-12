from pprint import pprint 

'''
7 2 9
6 6 6
5 5 7
'''

# 걍 무식하게 ㄱㄱ 걍 미리 좀 거를 수 있다는 거 걍 다 잊고 ... 
# 웅.. 제곱이라서... 너무... 내 머리로 생각해내기 어렵다 

# T = int(input())
# N, M, C = map(int, input().split())
# N = 꿀의 양
# M = 선택 가능한 개수 
# C = 꿀 최대 양 
N, M, C = 8, 3, 12

# honey_house = [list(map(int, input().split())) for _ in range(N)]
# honey_house = [
#     [7, 2, 9], 
#     [6, 6, 6], 
#     [5, 5, 7]
#     ]
honey_house =[
    [9, 1, 6, 7, 5, 4, 6, 7],
    [9, 5, 1, 8, 8, 3, 5, 8],
    [5, 2, 6, 8, 6, 9, 2, 1],
    [9, 2, 1, 8, 7, 5, 2, 3],
    [6, 5, 5, 1, 4, 5, 7, 2],
    [1, 7, 1, 8, 1, 9, 5, 5],
    [6, 2, 2, 9, 2, 5, 1, 4],
    [7, 1, 1, 2, 5, 9, 5, 7]]

# 한 행에서 연속해 집는다는게 힌트 
# 일단 M뭉치씩 집어
honey_bound_group = []
for i in range(N):
    for j in range(N-M+1): 
        honey_bound = honey_house[i][j:j+M]
        honey_bound_group.append(honey_bound)

# print(honey_bound_group) # 잘 나옴

# for honey_bound in honey_bound_group:
#     # 여기서 큰 순서대로 가져갈,,, 게 안되지 참 흑흐그흐그ㅡ 
#     honey_bound.sort()
#     honey_sum = 0 
#     i = 0
#     while honey_sum < C:
#         honey_sum += honey_bound[i]
#         i += 1

# honey_bound에 대해,, 어케해주면 좋을까
# 얘의 부분집합을 전부 구해서 부분집합의 썸이 C 이하인 걸 전부 데려온다음에 
# 각 요소들의 제곱들을 전부 더해주고 
# 이 최댓값을,, 남긴다? 나쁘지 않아
# honey_bound_group = [[6, 9, 2]]

'''
all_subset = []
for honey_bound in honey_bound_group:
    # honey_bound의 모든 부분집합을 구해준당 
    # 원소의 개수는 항상 M개로 동일할테니깐 
    M_honey_subset = []
    for i in range(1<<M): # 2^M이랑 하나하나 돌려가면서 비교할거야  
        subset = []
        for j in range(M): # 얘는 부분집합의 인덱스 자리
            # if i & honey_bound[j]: # 이부분이 잘못됐던거였어 
            # 그렇지 얘가 하나씩 밀려나가면서 맞는지 아닌지를 봐야하는거니깐
            if i & (1<<j):
                subset.append(honey_bound[j]) # 그 요소를 부분집합에 넣어줌
        M_honey_subset.append(subset)
    
    all_subset.append(M_honey_subset)

pprint(all_subset)
'''

all_subset = []
for honey_bound in honey_bound_group:
    # honey_bound의 모든 부분집합을 구해준당 
    # 원소의 개수는 항상 M개로 동일할테니깐 
    M_honey_subset = []
    for i in range(1, 1<<M): # 2^M이랑 하나하나 돌려가면서 비교할거야  # 공집합은 빼빼
        subset = []
        for j in range(M): # 얘는 부분집합의 인덱스 자리
            # if i & honey_bound[j]: # 이부분이 잘못됐던거였어 
            # 그렇지 얘가 하나씩 밀려나가면서 맞는지 아닌지를 봐야하는거니깐
            if i & (1<<j):
                subset.append(honey_bound[j]) # 그 요소를 부분집합에 넣어줌
        # 아냐 근데 이거... 내가 이따가 위치 겹치는지 아닌지 여부를 조회해줄 때,
        # 이 부분집합의 위치로 조회해줄 생각이었기 때문에,, 그냥 각 위치에 대한 모든 부분집합을 내비두긴 해야할거같음...
        # 아 상관이 없구나!!!!!! 이거 그 위치에서 만들어낸 M칸씩에 대한 부분집합이니깐 
        # 아 진짜 괜찮았어 아 이거 빼도 ㄱㅊ았네 어 좋다 

        # 애초에 처음부터 합이 C이하인 애들만 넣어줄래 
        # 수확할 수 있는 벌꿀의 양이 정해져있으니깐 이거 이하로만 수확할 수 있음 
        if sum(subset) <= C: 
            M_honey_subset.append(subset)

    all_subset.append(M_honey_subset)

pprint(all_subset)

# 그럼 이 all_subset을 순회돌면서 
# 제곱값을 저장할까? 
# 제곱값을 저장하는 배열을 만들어주자 

# 아니 안된다.. 내가 이미 저기서 걸르고 와서.. 안된다 힝 ㅜ 
# [[x for x in range(i*5+1, i*5+5)] for i in range(5)]
print([[x for x in range(i*5+1, i*5+6)] for i in range(5)])

honey_money_matrix = [[0]*N ]
