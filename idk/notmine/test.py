"""
20
4 5 3 4 2 4 4 3 5 2 2 3 5 5 5 2 5 2 5 5

"""
import sys
sys.stdin = open('namu_input.txt')

def find_min_days(sorted_tree, max_tree):
    i = 0
    day = 1

    while i < N:
        if sorted_tree[i] != max_tree:
            # print(f"현재 위치 i={i}, 지금의 날짜는 day{day} {sorted_tree}아직 물주기 전이야 이 홀짝에 맞춰서 와일문 맨끝에서 바뀔거야,,")
            # 이제 날짜의 홀짝 검출해야돼
            if day % 2 == 1:  # 홀수날
                # sorted_tree[i] += 1 # 이게 기본 로직, 모든 예외가 아닐 때 이거 그냥 무작위로 넣으면 됨
                # 예외) 근데 만약 두 칸 차이라면?
                if max_tree - sorted_tree[i] == 1:
                    sorted_tree[i] += 1
                    day += 1
                    i += 1
                elif max_tree - sorted_tree[i] == 2:
                    # 옆자리로 옮겨줘 얘는 옆이 마찬가지로 2 차이나도 ㄱㅊ아 내가 2먹고 옆은 1+1 하면 깔끔하니깐 ㅇㅇ
                    # 옆자리의 인덱스를 조회해야돼
                    if i + 1 < N:  # 옆자리가 인덱스 안에 있다면, 걔에게 물을 줌
                        sorted_tree[i + 1] += 1  # 물 주고
                        day += 1  # 날짜 주고
                        # 인덱스만 낫증가
                    else:  # 옆자리에 인덱스가 없다면
                        day += 1
                        # 물 안줌 = 인덱스는 낫 증가, 나무 낫 증가, 날짜만 증가
                else:  # 이 예외에 해당 안한다면?
                    # 그냥 물줘라
                    sorted_tree[i] += 1
                    day += 1
                    # 꽉 차기 전까지는 i 증가 ㄴㄴ
                    # i += 1
                # print(f"홀수날 증가확인 {sorted_tree}")
            else:  # day % 2 == 0: 짝수날
                # 예외) 만약 이 인덱스에 해당하는 놈이 한 칸 차이난다면?
                if max_tree - sorted_tree[i] == 2:
                    sorted_tree[i] += 2
                    day += 1
                    i += 1
                elif max_tree - sorted_tree[i] == 1:
                    # 옆자리로 옮겨줘
                    # 근데 이건 이제 1보다 더 큰 차이가 날 때까지 옆자리로 옮겨줘야 하는거지
                    k = 1
                    while k < N - i:
                        if sorted_tree[i + k] != max_tree and sorted_tree[i + k] != max_tree - 1:
                            break
                        k += 1
                    # 이 때의 k로 인덱스 조회를 해주면 됨
                    else:
                        day += 1
                        continue
                    sorted_tree[i + k] += 2  # 물 주는거야
                    day += 1
                    # 근데 옆자리에 물 준 거니깐 인덱스는 증가 안해
                # 예외가 아닌 나머지들은 전부 그냥 물줘
                else:
                    sorted_tree[i] += 2
                    day += 1
                    # 꽉 차기 전까지는 i증가 ㄴㄴ
                    # i += 1
                # print(f"짝수날 증가확인 {sorted_tree}")
        else:  # sorted_tree[i] == max_tree:
            i += 1  # 다음 인덱스로 가라
        # print(f"현재 위치 i={i - 1}, 지금의 날짜는 day{day - 1} {sorted_tree} 여기선 물줬어 ")
    return day


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_tree = max(tree)
    # 내가 해야하는 건 어차피 나무들의 키를 맞출 날짜밖에 없으니깐,,
    # 이거 그냥 내림차순해서 오른쪽으로 갈수록 키가 작으면 편하겠네
    # 일단 불안하니깐 원본 복제해주고
    # sorted_tree = tree[:]
    # 정렬
    tree.sort(reverse=True)

    ans = find_min_days(tree, max_tree) - 1
    print(f"#{tc} {ans}")