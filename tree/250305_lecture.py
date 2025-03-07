# 완전이진트리의 전위순회
def pre_order(n):
    if n <= N: # 이 n이 실존하는 정점의 번호여야함 # if T:
        print(n)            # visit(T)
        pre_order(n*2)      # pre_order(left[T]) = pre_order(T.left) # 같은말임
        pre_order(n*2+1)    # pre_order(right[T]) = pre_order(T.right)# 같은말임

# 함수에 N 넣는게 맞기는 함 근데 아래에서 선언이 돼서 ㄱㅊ나봐....


N = 9 # 완전이진트리 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] # 완전이진트리는 1번부터 시작하기 때문에 0번 인덱스는 사용 안하는거임

pre_order(1)