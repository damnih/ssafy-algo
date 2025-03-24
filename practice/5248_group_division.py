import sys
sys.stdin = open("5248_sample_input.txt", "r")

# 묶인 애들끼리는 그거임
# 사실상 같은 그룹으로 엮였다 이거 아님?!
# 전체 몇 개의 조가 만들어지는지 출력?
# 이거 일단 대표자 만들어서 set로 만들어 중복 처리해주면 되겠다
# 대표자는 어떻게 찾느냐
# 아,, 방금 배운 그걸 그대로 활용할까?
# 하고싶은대로 일단 해볼까?


def get_rep(x):
    if parents[x] == x:
        return x
    # 그거뭐냐 그
    # 부모의,, 그거
    # 부보의,,,
    # 나의 부모를 찾는데
    # 그 부모의 부모를 찾고
    # 부모의 부모를 찾고
    # 즉,, 어떤 x의 코어 부모는,, 부모 찾는 연산을 재귀로 계속한 것!!!
    parents[x] = get_rep(parents[x])
    return parents[x]

# 내가 뭘 놓쳤느냐.. 그니깐 같은 집합으로 묶어주는 걸 안했네 ㄱㅡ
# 그니깐 나는 부모만 따져준거고,,
# 대표자를 찾은건,, 아니네 !!!
def union(x, y):
    root_x = get_rep(x)
    root_y = get_rep(y)

    if root_x == root_y:
        # 이미 같을 경우.. 머 해줄게 없네?
        return

    if root_x < root_y:
        parents[root_y] = root_x

    if root_x > root_y:
        parents[root_x] = root_y

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 사람의 머릿수가 N명임
    # 신청서는 M장임

    # 이거 그냥 포문 돌려가면서 즉석에서 ref 바꿔주면 되는 거 아닌가?
    # 근데 대표자인데 왜 ref임? representative일줄 알았는데 reference인가?
    # 할튼,, 일단 대표자들을 생성하는 것부터 해주자!

    parents = [i for i in range(N + 1)]
    # print(parents)
    # 걍 왼쪽에 받아주는 번호를 무조건 부모라고 치고 입력으로 받아주장

    info = list(map(int, input().split()))
    for i in range(M):
        p = info[2*i]
        c = info[2*i+1]
        # p, c = map(int, input().split())
        # c인덱스를 가진 곳에 c의 부모가 누구인지 입력
        # parents[c] = p # 이거 살린 채 union(p,c)를 했을 때 런타임에러뜸 망함 안됨
        # 왜 안될까? 직접 써보면서 확인해보자,,
        union(p, c)

    # print(parents)


    for i in range(1, N + 1):
        parents[i] = get_rep(i)
    # print(parents)

    rm_dupli = set(parents)
    ans = len(rm_dupli) - 1 # 0인덱스 버려줘야 하니깐 ㅎㅎ
    print(f"#{tc} {ans}")

