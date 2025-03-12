
그래프 (데이터 간 관계가 존재한다면,,)
DFS BFS

근데 N이 너무 크다면,,
새로운 알고리즘이나 자료구조를 고민해야함

- 재귀 호출 접근법의 경우
백트래킹(가지치기) <- 더 이상 보지 않아도 되는 경우는 쳐내자

- 정렬하는 경우 (sort)
최소값/구간, 최대값/구간 등
내장함수 sort는 O(NlogN)이 보장됨
탐색해야 한다: 이진 탐색 << 아 이거 진짜 어카냐고.......

- cf 심화 문제들
최단 거리: dijkstra
최소 비용: MST

위의 방법들은
한번한번 마다 시간이 필요한데
한번 만들어놓고 여러번 조회해도 되는 경우들이 있음
자료구조 문제들이 대부분 이런 경우
- 이진 탐색 트리
- 힙(우선순위 큐)
- 그룹화(UNION-FIND)
- Trie, segment tree ...

* 우리 커리큘럼에서는 이 그룹화 유니언파인드까지,, 배움,, A형 범위가 이러하다...



------
# 재귀함수 설명 시작
------

N중포문이 필요한
반드시 알아야할 함수의 특징

메인은 그냥 전역,,
케이에프씨라는 함수가 있다고 가정

3이라는 값을

,,,


def KFC(x):
    print(x)
    x += 1
    print(x)


재귀의 조건을 안주고 끝까지 들어가면,,
파이썬의 재귀 한계까지 감,,
대략 1000정도래