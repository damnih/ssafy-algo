

# 기준이랑 같은 수를 처리할 때 등호를 빼는 게 걍 처리안하고 연산 줄어서 좋다고 생각했는데,
# 1 1 1 1 1 0 0 0 0 같은 거 처리하려면 등호 넣어줘야되겠구나

# def partition(arr):
#     # 그니깐 가장 효과적인 파티션을 만들어주는 함수인거잖아,,




def quick_sort(arr, start, end):
    # 그 머냐 이거 끝나는 조건 여기에 달아줘야함
    if start < end:
        # left = start
        # right = end
    # if len(arr) > 1:
    #     으로 할까? 근데 이거 좀 에바인 거 같은데...
    #     왜냐하면 이러면 리턴을 계속 배열을 해줘야해
    #     근데 리스트 슬라이싱은 시간 오래 걸린댔잖아
    #     고로 걍 인덱스만 반환하고 넣어주고 하면 될 듯
    #     즉 시작과 끝이 같으면 끝나는 거임
        # 퀵 소트의 개념은??
        # pivot 기준 하나 정해
        pivot = where_pivot(start, end)
        quick_sort(arr,start, pivot - 1)
        quick_sort(arr, pivot +1, end)

        # 이 기준값과 비교해서
        # 하나는 왼쪽에서부터 순회하며, 기준보다 작으면 냅두고, 크면, 멈추고
        # 하나는 오른쪽에서부터 순회하며, 기준보다 크면 냅두고, 작으면, 멈추고
        # 그러다가 왼쪽에서부터 오는 i 랑 오른쪽에서부터 오는 j가 교차되면,
        # 그 때 멈춤!!!!
        # 그 교차되는 위치가 pivot이 위치할 자리인 것임~~~
        # 나는 맨 왼쪽에 있는 녀석으로 해줬으니깐,
        # 교차된 이후의 j 위치랑 교환해주면 되겠당
        #
        # 이 i j 는 이 안에서 정의해서 옮겨주는 정도고,
        return arr
def where_pivot(left, right):
    pivot = left

    i = left + 1 # 피벗보다 한칸오른쪽 ㅇㅇ
    j = right
    while i <= j:

        while data[i] <= data[pivot]:
            i += 1
            if i > j:
                break

        while i <= j and data[j] >= data[pivot]:
            j -= 1

        if i < j:
            data[i], data[j] = data[j], data[i]

    data[pivot], data[j] = data[j], data[pivot]

    return j
    #         if i <= j and arr[i] >= pivot:
    #             # 왼쪽에서 오는 애라, 기준보다 작아야함.
    #             # 작을 떈 스루, 클 때만 처리
    #             # 자리를 j랑 바꾸어줄건데 여기서 j 같이 조회햇나욤?
    #             if i <= j and arr[j] <= pivot:
    #                 # 오른쪽에서 오는 애라, 기준보다 커야함.
    #                 # 고로 작을 때만 처리해주면 됨
    #                 arr[i], arr[j] = arr[j], arr[i]
    #             else:
    #                 j -= 1
    #                 # if i > j:
    #                 #     arr[left], arr[j] = arr[j], arr[left]
    #                 # 어차피 와일문 탈출이라 없어도 됨
    #
    #         # elif i <= j and arr[j] <= pivot:
    #
    #         # 그니깐 이 i가 움직이는 것과 j가 움직이는 건 완전히 다른 영역이거든?
    #         # 근데 i에 뭐가 걸릴때,
    #         # j또한 뭐가 걸렸다면,
    #         # 자리를 바꿔라~ 하는 거잖아
    #         # 이 의문은 저 위에서 if 두번 써서 해결한듯
    #
    #         # 만약 i나 j 둘 중 하나에 뭐가 걸렸는데,
    #         # 다른 하나는 안 걸려서 그냥 인덱스만 쭉 옮겨간다면
    #         # 그냥 그대로 교차점 생성돼서 피벗 위치 정해지는 거구,,,
    #
    #         # 하.. 근데 이거는 or이니깐, 선j부터 봐주는 경우도 작성을 무식하게 해줘야하나?
    #         # 까짓거 함 해보죠
    #         elif i <= j and arr[j] <= pivot:
    #             # 왼쪽에서 오는 애라, 기준보다 작아야함.
    #             # 작을 떈 스루, 클 때만 처리
    #             # 자리를 j랑 바꾸어줄건데 여기서 j 같이 조회햇나욤?
    #             if i <= j and arr[i] >= pivot:
    #                 # 오른쪽에서 오는 애라, 기준보다 커야함.
    #                 # 고로 작을 때만 처리해주면 됨
    #                 arr[i], arr[j] = arr[j], arr[i]
    #             else:
    #                 i += 1
    #                 # if i > j:
    #                 #     arr[left], arr[j] = arr[j], arr[left]
    #                 # 이건 없어도 됨 어차피 와일문 탈출이야 ㅇㅇ
    #         else:
    #             # 이 조건을 걸리든 말든 무조건 할 건 뭐다?
    #             # 인덱스 증감
    #             i += 1
    #             j -= 1
    #
    #     # 이 퀵소트는 사실상 재귀의 형식이긴 함
    #     # 리스트의 길이가 1이 될 때까지,, 최소단위가 될 때까지 반복해서 해주는 거니깐
    #     # 퀵소트를 해서 나온 반띵된 작은부분 큰부분들에 대해서 계속 퀵소트를 돌리는 거지
    #     # 아 잠만 이건 파티션을 나누는 그거인가?
    #     # 그니깐 파티션을 나누는 함수를 따로 만들어준다음에
    #     # 그 함수의 결과로 나온 레프트 라이트에 대해서
    #     # 퀵소트를 돌리는 걸까?
    #     # 엉.. 그런거같아
    #     # 헐
    #     # 그렇다면;;
    #     arr[left], arr[j] = arr[left], arr[j]
    #
    #     # 이렇게 정렬하면 피벗의 위치는 정해짐
    #
    #     # 피벗을 기준으로 좌구간 우구간 나눠서, 다시 이거 돌려주면 됨
    #     quick_sort(arr, start, j-1)
    #     quick_sort(arr, j+1, end)
    #     # 언제까지? 리스트 길이가 1이 될 때까지 즉 단위크기가 될 때까지
    # return

data = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
e = len(data)
quick_sort(data, 0, e - 1)
print(data)
