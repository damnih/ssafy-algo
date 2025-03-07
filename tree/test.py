# 만약,, 내 아래로 몇 개의 정점이 있는지 알 고 싶어~!
def cnt_pre_order(T):
# 0이 아니면(존재하는 정점이면)
    global cnt
    if T:
        print(T)    # visit(T) T에서 할 일 처리
        cnt += 1
        cnt_pre_order(left[T]) # 왼쪽 자식(서브트리)로 이동
        cnt_pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동


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


cnt = 0
cnt_pre_order(3)
print(f"카운트는 {cnt}")
