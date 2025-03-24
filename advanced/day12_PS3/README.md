# 2025-03-21(금) 문제풀이 3 라이브 문제 목록

- 1251. 하나로
    - [문제 바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD)
    
- 1249. 보급로
    - [문제 바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD)
    
- 4012. 요리사
    - [문제 바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH)
    
- 4008. 숫자 만들기
    - [문제 바로가기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH)

---

## 정리
MST(최소 신장 트리)
  - 양방향 그래프에서 최소한의 간선으로
	모든 노드를 연결하는 트리
	(노드의 수 N개 일 때 N-1의 간선)

  - Prim: 정점을 기준으로 작은 가중치부터 고르자
    - 우선순위큐가 사용됨
    - 시간복잡도: ( VlogV + ElogV )
	- VlogV: 보통 E가 더 크기 때문에 생략
	- ElogV: E개의 간선을 우선순위 큐에 넣는 시간
	-> 힙 트리의 높이가 최적화를 하지 않아도
	    logE 만큼 높아지지 않는다.
	-> 그 만큼 시간이 빨라진다.
     - 결론: 정점에 비해 간선이 많을수록 유리하다!!!!
		

  - Kruskal: 간선을 기준으로 작은 가중치부터 고르자
    - 정렬이 사용됨
    - 간선이 E 개 => 시간은 O(ElogE)
		+ 사이클 검사(유니온파인드)
		-> 거의 상수
    - 결론: 정점에 비해 간선이 적을수록 리하다!!!!


최단 거리
  - Dijkstra
  - 최장거리 문제 못 풉니다.
   - 더 긴 거리는 미리 확정지을 수 없다.
     - 그리디로 접근하면 틀립니다.


정점에 비해 간선의 수가 많으면 prim 이 유리하다.
얼마나 있어야 많은걸까 ???

정점의 수 = V

```
- 간선의 수가 V 이하 == 간선의 수가 적다

- 간선의 수가 VlogV == 적당히 존재한다.

- 간선의 수가 V^2/2 == 모든 노드가 연결되었다 == 수가 많다
```

