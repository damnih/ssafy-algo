'''
아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이되는 부분집합을 모두 출력하시오.
'''
'''
-1 3 -9 5 -7 -6 1 5 4 -2
'''


'''
# arr = list(map(int, input().split()))
arr = [-9, -7, -6, -2, -1, 1, 3, 4, 5, 5]  # 아웃풋 보니깐 앞의 오와 뒤의 오는 다른 오 취급함 ㅇㅇ
# arr.sort()
# print(arr)

# print([1, 2, 3, 4] == [2, 3, 4, 1]) # False 

pos_arr = []
neg_arr = []
zero = []

# 일단 배열의 수들을 종류에 따라 나눠준다
for num in arr:
    # 0은 있다없다 두개의 경우의수들이 곱해짐. 즉, (0이 아닌애들의 부분집합 개수) * (2**(0의개수))
    # if num == 0: 
    #     zero.append(num) # 개수만 셀 거 아니니깐 걍 이거 0 양수에 포함시키자 귀찮다 
    if num >= 0:
        pos_arr.append(num)
    # elif num < 0:
    else:
        neg_arr.append(num)

# 오름차순 정리된 애들로 받았으니깐 음수애들은 머 그대로 들어올거고 양수애들만 내림차순으로 바꿔줄까 ㅎㅅㅎ
pos_arr.sort(reverse=True)

# print(neg_arr) # [-9, -7, -6, -2, -1]
# print(pos_arr) # [5, 5, 4, 3, 1]


# 일단 음양수합차 생각해봐 
# 음수합은 -25 양수합은 18 
# 아무리 커져도 18보다 커지면 안돼 
# 일단 음수의 부분집합을 구할때 18보다 커지면 만들지 말자 

# 그리고 음수와 양수의 각각 부분집합들을 뽑아내서 
# 각각의 합을 보고 abs가 같으면 리스트 합쳐 
# 그게 0이 되는 부분집합임 
# 걔네들 전부 0이 되는 부분집합 수로 넣어 

neg_n = len(neg_arr)
# 일단 음수들의 부분집합을 만들어줄거임!! 
# 근데 이거 진짜 부분집합을 다 만들기보다 어차피 합만 보면 되는거 아닌가? 
# 아 아니네,, 이거,, 부분집합을 출력하라 그러네,,  
# 이거 부분집합 만드는 로직 똑같이 써서 집합에 추가하는 부분만 걍 sum에 추가하면 되지 않으려나,,
# 아니야 합 두는 거 ㄱㅊ은거 같아 왜냐하면 부분집합이랑 인덱스가 같으니깐 
# 이거 정렬 없이 걍 돌면서 있으면, 그 인덱스에 해당하는 부분집합 끌어다가 추가하면 됨 ㅇㅇ! 
neg_sub_sum = []
neg_sub = []
for bin in range(1 << neg_n): # 2^n까지 나올 이진수에 대해서~~~ 
    sum = 0
    subset = []
    for i in range(neg_n): # 자릿수를 돌려줄거야,,
        if bin & (0x1 << i): # 각 자릿수가 1과 같다면,, 
            sum += neg_arr[i]
            subset.append(neg_arr[i])
            # if sum > sum[pos_arr]:
            #     sum -= neg_arr[i]
            #     neg_sub_sum.append(sum) # 아니야 이 로직 삭제하자 ㅜㅜ 괜히 헷갈린다 ㅜㅜ 
    # 이 자릿수를 도는 for문이 끝나면,,
    # 각 이진수에 해당하는 sum이 나와야 함 ㅋㅋ ㅜㅜ 
    neg_sub_sum.append(sum) # 잘나옴 
    neg_sub.append(subset) # 잘나옴

# print(neg_sub_sum)
# print(neg_sub)

# 같은 방식으로 양수도 ^^! 
pos_n = len(pos_arr)

pos_sub_sum = []
pos_sub = []

for bin in range(1 << pos_n):
    sum = 0
    subset = []
    for i in range(pos_n):
        if bin & (0x1 << i):
            sum += pos_arr[i]
            subset.append(pos_arr[i])
    pos_sub_sum.append(sum)
    pos_sub.append(subset)

# print(pos_sub_sum)
# print(pos_sub)

# 아 이건 진짜 새삼.. 2^5라 살았다.. ^^ 

for i in range(len(pos_sub_sum)):
    for j in range(len(neg_sub_sum)):
        if pos_sub_sum[i] + neg_sub_sum[j] == 0:
            zero_subset = pos_sub[i] + neg_sub[j]
            print(zero_subset)
'''

# ... 근데 이거 아무리 생각해도 그리디의 이점을 못살렸는데? 
# 완탐을 두번.. 세번.. 한것밖에 더 돼?
# 그냥.. 첨부터 했음 나았을거 같다.. ^^ 
# 그래... 걍 있는 집합 돌려서 하자 비트연산 연습하고 좋지 ^_^ 

arr = list(map(int, input().split()))
# print(arr) 
# arr = [-1, 3, -9, 5, -7, -6, 1, 5, 4, -2]

n = len(arr)
# fullset = []
for bin in range(1 << n):   # 이 하나씩의 이진수에 대해 
    subset = []
    sum = 0
    for i in range(n):      # 자리 위치를 n만큼 옮겨가며
        if bin & (1 << i):  # 1이랑 같으면
            subset.append(arr[i])
            sum += arr[i]
    # 여기서 이제 출력해주는거임 각 bin마다 비교해서 나온 서브셋이 있잖아?
    if sum == 0:
        print(subset)

# print(len(fullset)) # 45 
# 답도 45 맞음 

# ans = list(input().split())