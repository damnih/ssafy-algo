# 서로소 집합의 기본 개념 및 정리

#
# 필요한 것은...
# 1. 대표자로 설정하는 것
# 2. 묶었을 때 대표자가 누구인지 확인하는 것
# 3. x, y를 하나의 집합으로 묶는 것
#
#
# 1~ 6까지,, 6개의 원소가 존재하는 경우
#
# 1. 각 집합을 만들어주는 함수가 필요
def make_set(n):
    # 1~6까지의 원소가 있다고 가정, 총 n개의 집합을 생성
    # --> 각 원소의 부모(!= 대표자) (대표자와 부모는 다른 개념임)를 자기 자신으로 초기화
    parents = [i for i in range(N+1)]
    return parents

# 2. 이제 부모 찾으러 가는 거임
def find_set(x):
    # 찾으려던 값이 위치한 곳은 parents[x]
    # 근데 이걸 반복하고 반복하고 반복하겠지
    # 부모를 찾으면 그 부모의 부모를 찾고
    # 또 그 부모의 부모의 부모를 찾고
    # 이런 식으로 꼐속 타고타고타고타고 타고들어가겠지
    # 그렇다면 언제 끝나?
    # parents[x] = x이 될 때 끝나는거임 ㅜ
    # 고로 내가 찾아낸 부모가 다시 인자로 들어간다

    # 내 부모 == 나 일때 결국 걔가 대표자인 거라서 ㅇㅇ
    if parents[x] == x:
        return x

    return find_set(parents[x])
    # 근데 이게 언제 끝나? if parents[x] == x: 일때인거임



# 3. x, y를 하나의 집합으로 묶는 것..
def union(x, y):
    # 일단 하나의 집합으로 묶으려면..
    # 같은 집합인지 다른 집합인지 확인부터 해야해
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 같다면,,
    if rep_x == rep_y:
        return # 걍 같은 집합이면 그대로 끝
    # 아니라면..
    # 합치러 가야지...
    # 문제에 따라 우선되는 집합으로 합쳐주면 됨!!
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    if rep_x > rep_y:
        parents[rep_x] = rep_y
    # 같은 집합으로 합쳐준다는 뜻은 이 대표자가 같다는 뜻임!!!!!
    # 그러니깐 이렇게 해주는 거엿음!!!!1

N = 6
parents = make_set(N)

union(1, 2)
union(2, 3)
union(5, 6)

print(parents)


### 이 아래로 활용~!
if find_set(3) == find_set(5):
    print("같은 집하빕니다,")
else:
    print("다른 집합입니다,")
    