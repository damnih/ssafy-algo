#
#
#
# def merge(left, right):
#
#     while i < len(left):
#         i += 1
#
#
#
# 아니 아까 퀵소트 범수랑 했던거에서 비슷하게 했잖아
# 이건 병렬적으로 각각 가는거야
# 그렇다면,,
#
# 아 앞에거 보고 살짝 눈치챔
# 그니깐 조회는 i j 를 같이 하는데
# 각각이 증가하는건 병렬적으로 저마다 하는 거잖아?
#
# 하 결국.. 완성 코드 보고 걍 따라함 ㅜ
# 케이스 어케 나누나 하고 실눈뜨고 봤는데 거의 80퍼 다 봐버렸다 ㅜ
# 기억이 너무 생생해,,, 띠밤


def merge(left, right):
    i = j = 0
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        if left[i] > right[j]:
            merged_list.append(right[j])
            j += 1
        # 얘네들은 둘 다 if로 가줘야해
        # 왜냐하면 내가 위에서 i를 증가시킨 채 끝내줬기 때문에
        # 이미 하나 어펜드한거면 인덱스는 다음걸로 넘어갔고
        # 그 넘어간 인덱스랑 아래 j랑 비교하는 거라서 ㅇㅇ
        # j 또한 같음 !!
    # 인덱스 넘어가서 와일문 반복이 끝나면,,,
    # 정렬안하고 넘어간 남은 리스트 뒤에 추가해줘야겠지?
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    # 리스트 슬라이싱의 신기한 점,
    # 슬라이싱을 할 땐 인덱스 범위를 넘어서 있는 걸 조회해도 오류가 일어나지 않아~!
    # 그냥 슬라이싱 할 거 없다고 넘겨짐!!!
    return merged_list

# 근데 이걸 리턴하면,, 어케함?
# 리턴해서,, 어따써?
# 그니깐 그게 ,,
# 어케활용됨?


def merge_sort(arr):
    if len(arr) == 1:
        return

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # 재귀를 어디서 돌려줘?
        # 잘 생각해보자
        # 나는 이 쪼개는 걸 계속계속 반복하고 싶은 거야 ㅇㅇ
        # 그니깐 통째로의 리스트를 왼 오 로 잘랐고
        # 그뒤에 또
        # 왼을 왼 오 로 잘르고
        # 오를 왼 오 로 자르고
        # 이에 대한 놈들을 또 왼 오로 자르고
        # 이걸 반복하는 거잖아?
        # 고로 머지 소트를 반복하는 거다
        # 머지 소트를 여기서 호출 반복하는 거임!!!!!

        # merge_sort(left)
        # merge_sort(right)
        # 근데 얘네를 할당을 해줘야지? 뭐겠어?
        # 정리된 left right을 또 합쳐서 최종정렬이 되는 걸거잖아?

        left = merge_sort(left)
        right = merge_sort(right)
        # 이렇게 할당을 해주고
        # 이 녀석들에 대해서 merge를 해주는거임

        merge(left, right) # 얘를 소환하면 렢라가 합쳐진 하나의 배열이 반환됨


    # 아니 근데 이러면,, 그거잖아
    # 재귀를 쓸 곳이 없잖아,,
    # 재귀를 써서 계속 계속 계속 ,, arr의 길이가 1이 될 때까지 얘를 잘라줘야 하는데


