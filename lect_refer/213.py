def inorder_traversal(node, n, tree, result):
    if node > n:
        return
    # Left child
    inorder_traversal(node * 2, n, tree, result)
    # Current node
    result.append(tree[node])
    # Right child
    inorder_traversal(node * 2 + 1, n, tree, result)


def solve():
    T = int(input())  # 테스트 케이스 개수
    for t in range(1, T + 1):
        N = int(input())  # 완전 이진 탐색 트리의 노드 개수
        # 트리에 1부터 N까지의 숫자를 저장
        tree = [0] * (N + 1)
        for i in range(1, N + 1):
            tree[i] = i

        result = []
        inorder_traversal(1, N, tree, result)

        # 루트와 N/2번 노드의 값을 출력
        root_value = result[0]  # 중위 순회 결과의 첫 번째 값이 루트 노드
        mid_value = result[N // 2 - 1] if N // 2 <= len(result) else None

        print(f"#{t} {root_value} {mid_value}")


# 실행
solve()
