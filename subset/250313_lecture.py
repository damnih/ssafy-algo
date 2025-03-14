
# 일단 경우의 수는 (2^n = 1<<n)

# 이 범위의 이진수에 대해서 각 이진수로 순회를 돌려줄거임 

mom_set = ['A', 'B', 'C', 'D', 'E']
full_subset = []
n = len(mom_set)

for bin_num in range(1 << n):
    # 여기서 뽑혀나온 애는 한 이진수임 
    # 이 이진수마다의 subset이 필요
    subset = []
    for i in range(n): # 그 이진수의 n번째 자리에 대해,,
        if (bin_num) & (0x1): # 여기가 애매하긴 해 이러면 알아서 옆까지 움직이나? 아닐거같은데,,
        # if bin_num & (0x1<<(n-1)): # 이것도 아님 
        # if (bin_num << i) & (0x1):  # 힝 이것도 안돼 ㅜ 

            subset.append(mom_set[i])
    full_subset.append(subset)

print (full_subset) 



#### 위에 있는 코드는 내거인데 틀렸어 ㅜ 
# 강사님 코드 다시 봐보장 


arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)



# 1인 비트 수를 반환하는 함수 
def get_count(tar):
    cnt = 0
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1
    return cnt 



# # 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수 
ans = 0
# 모든 부분 집합을 확인 
for target in range(1 << n):
    # 만약, 원소의 개수가 2개 이상이면, 답 += 1 
    if get_count(target) >= 2:
        ans += 1
print(ans)

