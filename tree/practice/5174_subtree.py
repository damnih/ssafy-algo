# 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 구해라 ,,
# 이거 N으로 시작하는,, 전위 순회!!! 하면 되는 건가??!

'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

def count_lec_jun(T): # 1줄
    global count
    if T:
        # print(T) # 2줄
        count += 1
        count_lec_jun(left[T]) # 3줄
        count_lec_jun(right[T]) # 4줄
    return count

# # 아 이해했어 if T 로 쓰면서 불린값 트루펄스를 따지는 거구나

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split()) # N은 루트임 맨 위에 있는 녀석
    # E개의 부모 자식 노드 번호 쌍
    # 노드 번호는 1번부터
    node_list = list(map(int, input().split()))
    # 받은 배열 안에 있는건,,
    # 노드의 ,, 값?!
    # 근데 여기서는 노드의 값이 곧 이름이자
    # 아 그냥 저 정점값의 최대를 찾아서 해주면 될.. 듯?!
    M = max(node_list)
    left = [0] * (M + 1)
    right = [0] * (M + 1)

    for i in range(E):
        par_num = node_list[2 * i]  # 부모임
        chil_num = node_list[2 * i + 1]  # 자식임
        if left[par_num] == 0:
            left[par_num] = chil_num
        else:
            right[par_num] = chil_num
    count = 0
    ans = count_lec_jun(N)
    print(f"#{tc} {ans}")
    # 노드 N을 루트로 하는 서브트리에 속한 노드의 개수
    # N을 중심으로 전위 순회 돌면 됨


# 노드 번호는 E+1 번까지 존재한다는데 이걸,, 활용할수있는지 내가 생각한 방식으로 할 수 있는 게 맞는지 모르겠음,,
# 그니깐 나의 구현 방법은,,
# 부모값을 인덱스로 가지는 위치에 자식을 배치시키는 거란 말임,,
# 그래서 부모의 값이 곧 배열의 길이가 되기 때문에,,
# ,, 이게 되려면 받아온 노드 리스트의 최댓값이 E여야 하는 거 ,, 아닐까? ㅜㅜ
# 이 고민을 하는 이유,, 사실 별 생각 없었는데 옆의 범수님이 배열의 길이를 E+1로 두었음
# 이거,, 물어봐야됨

# 부모, 자식
# 이렇게 간대

# for i in range(E):
#     par_num = node_list[2 * i] # 부모임
#     chil_num = node_list[2 * i + 1] # 자식임
#     if left[par_num] == 0:
#         left[par_num] = chil_num
#     else:
#         right[par_num] = chil_num

# print(left)
# print(right)
# 잘나옴!

# 노드 N을 루트로 하는 서브트리에 속한 노드의 개수
# N을 중심으로 전위 순회 돌면 됨

def jun_order(num):
    print(num)
    if left[num] != 0:
        jun_order(left[num])
        jun_order(right[num])

# jun_order(1)



# 아니 머릿속에 남아있어
def lec_jun(T): # 1줄
    if T:
        print(T) # 2줄
        lec_jun(left[T]) # 3줄
        lec_jun(right[T]) # 4줄

# if T가 무엇을 의미하는 건지 모르겠어,,
# if T: 조건문은 현재 노드 T가 존재하는지 확인합니다.
# 여기서 T는 노드의 값이나 참조를 나타냅니다.
# 이 조건이 필요한 이유는 다음과 같습니다:
# 1) 종료 조건: 이진 트리의 전위 순회에서 더 이상 탐색할 노드가 없을 때,
# 즉 T가 None(또는 비어있음)을 의미할 때 재귀 호출을 중단하기 위해 필요합니다.
# 2) 유효성 검사: T가 유효한 노드일 경우에만 해당 노드의 값을 출력하고,
# 왼쪽 및 오른쪽 자식 노드로 재귀 호출을 진행합니다.

# lec_jun(1)

# 이거였단말야 이게 전부였어...
# 근데 얘의 원리를,, 아직 이해하지 못했어,,,
# 아 알겠다
# 이거 1줄 하고
# 2줄 프린트하고
# 3줄 지나가면 왼쪽 자식을 넣은채 다시 함수 호출해서 1줄로 돌아감
# 1줄 - 2줄 가면서 그 왼쪽 자식을 다시 출력해
# 그러고 다시 3줄에서 함수 호출해서 1줄로 넘어가고,,
# 이걸 반복하면서 왼쪽애를
# 근데,, left[T]가 없으면 오른쪽으로 넘어간다,, 는 말이라도 넣어줘야 하는 거 아닌가?!
# 그거 이프문 안써도 돼...? ㅜㅜ < = 안 쓰기 위한 게 if T:였음,,
# 확인해보니 안썼어,, 그렇다면 이걸로 돌아간대.. 근데 어케 레인지오류 안나고 이러지 ㅜㅜ

