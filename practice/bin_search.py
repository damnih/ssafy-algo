arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용해야 한다
# 그 이유는 알지?? 왼작 오큰
arr.sort()

def binary_search_while(target):
    left = 0
    right = len(arr) - 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return -1, cnt

def bin_search_recur():
    # left, right를 작업 영역으로 검색
    # left <= right 만족하면 반복
    if left > right:
        return -1

    mid = (left + right) // 2
    if target == arr[mid]:
        return mid

    # 작다면 왼쪽구간 탐색
    # 크다면 오른쪽 구간 탐색