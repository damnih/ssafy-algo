'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

13
2 1 2 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# # # 이거 재귀함수 형식인거지?

# 여기서 만든 건 본인과 자손들에 대해서만 순회를 돌린 거임
def pre_order(T):
# 0이 아니면(존재하는 정점이면)
#     global cnt
    if T:
        print(T)    # visit(T) T에서 할 일 처리
        # cnt += 1
        pre_order(left[T]) # 왼쪽 자식(서브트리)로 이동
        pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동

# 만약,, 내 아래로 몇 개의 정점이 있는지 알 고 싶어~!
def cnt_pre_order(T):
# 0이 아니면(존재하는 정점이면)
    global cnt
    if T:
        print(T)    # visit(T) T에서 할 일 처리
        cnt += 1
        cnt_pre_order(left[T]) # 왼쪽 자식(서브트리)로 이동
        cnt_pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동




def in_order(T): # 중
    if T:   # 0이 아니면(존재하는 정점이면)
        # cnt += 1
        in_order(left[T]) # 왼쪽 자식(서브트리)로 이동
        print(T)    # visit(T) T에서 할 일 처리
        # 왜 이 프린트 위치가 바뀌느냐, 여기서 inorder에 넣어주는 것으로 T값이 변화를 해
        # 그러니깐 이 변화했을 때의 T를 출력을 해줘야, 탐색 순서에 맞춰서 출력이 나와줌
        in_order(right[T]) # 오른쪽 자식(서브트리)로 이동

def post_order(T): # 후
    if T:   # 0이 아니면(존재하는 정점이면)
        # cnt += 1
        post_order(left[T]) # 왼쪽 자식(서브트리)로 이동
        post_order(right[T]) # 오른쪽 자식(서브트리)로 이동
        print(T)    # visit(T) T에서 할 일 처리
        # 왜 이 프린트 위치가 바뀌느냐, 여기서 inorder에 넣어주는 것으로 T값이 변화를 해
        # 그러니깐 이 변화했을 때의 T를 출력을 해줘야, 탐색 순서에 맞춰서 출력이 나와줌



N = int(input()) # 1번부터 N번까지인 정점
E = N - 1 # 간선 수
arr = list(map(int, input().split()))

left = [0] * (N+1) #
right = [0] * (N+1) #
par = [0] * (N+1) # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i+1]
# 이런건 약간 자식의 왼오 순서를 정해야할때 이렇게 나눠주면 됨
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# print(left)
# print(right)

root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
        break
pre_order(root)


cnt = 0
cnt_pre_order(3)
print(f"카운트는 {cnt}")


# pre_order(3)




