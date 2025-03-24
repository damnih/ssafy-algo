# left, right : 작업 범위

def quick_sort(left, right):
    if left < right:
        # pivot 기준으로 정렬시킨다.
        # 파티션 나누는 다른 함수가 필요
        pivot = partition(left, right)
        # 왼쪽 진행
        quick_sort(left, pivot - 1)
        # 오른쪽 진행
        quick_sort(pivot + 1, right)

    pass



arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

def hoare_partitioning():
    pivot = arr[left]

    i = left + 1
    j = right
    while i <= j: # 교차하지 않는 범위 내에서
        # i는 오른쪽으로 진행하면서, 기준보다 큰 값을 찾음
        # 고로 j를 만나 스왑되기 전까지, 피봇보다 계속 작은 값이라면 진행
        while i <= j and arr[i] <= pivot:
            i += 1
        # j는 왼쪽으로 진행하면서, 기준보다 작은 값을 찾음
        # 고로 i를 만나 스왑되기 전까지, 피봇보다 계속 큰 값이라면 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 이렇게 가다가 발견하면, 자리 스왑

        # 피벗, 제일 왼쪽 요소,
        # 피벗, 제일 오른쪽 요소,
        # 이렇게 방향 반대로 해서 또 짤 수 있음
