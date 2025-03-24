def make_set(N):
    # 1~N까지의 원소가 있다고 가정 -> 총 n개의 집합을 생성
    # 각 원소의 부모(!=대표자)를 자신으로 초기화
    parents = [i for i in range(N+1)]
    return parents
    #패런츠를 전달받아서 여기서계속 갱신하며 패런츠를 관리해볼거임


def find_set(x):
    find_set(parents[x])



def union(x, y):


N = 6
parents =make_set(N)
