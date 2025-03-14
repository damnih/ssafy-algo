'''
1 2 1 3 2 4 2 5 3 6 3 7 4 8 4 9 6 10 6 11 7 12 10 13 10 14
'''


arr = list(map(int, input().split()))

N = 14 # 정점 수
E = 13 # 간선 수

left_tree_arr = [0] * (N + 1)
right_tree_arr = [0] * (N + 1)

# 간선 수 13
for i in range(13):
    parent = arr[i * 2]
    child = arr[i * 2 + 1]
    if left_tree_arr[parent] == 0:
        left_tree_arr[parent] = child
    else:
        right_tree_arr[parent] = child


def jung_order(T):
    if T:
        jung_order(left_tree_arr[T])
        print(T)
        jung_order(right_tree_arr[T])

jung_order(1)
print("이 아래로는 3에서부터 시작 확인")
jung_order(3)
print("이 아래로는 6에서부터 시작 확인")
jung_order(6)