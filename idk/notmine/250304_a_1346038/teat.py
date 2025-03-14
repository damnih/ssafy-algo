sorted_tree = [8, 8, 7, 7, 7, 7, 7, 7]


N = len(sorted_tree)
i = 2
k = 1
max_tree = 8

while k < N - i:
    if sorted_tree[i + k] != max_tree - 1:
        break
    k += 1

print(k)

# i + k = 2 + 3 = 5
# 인덱스 반환 잘됐는데??
