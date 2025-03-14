# [0, 1, 2] 3개의 카드가 존재
# 2개를 뽑을 예정

# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
# 뽑은 카드들을 저장
path = []
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 2:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return # 그냥 이렇게 리턴만 적어도 알아서,, 리턴값이 나옴 재귀함수 그자체를 반환하니깐 ㅇㅇ
    # # 1. 1개의 카드를 뽑는다
    # path.append(0)
    # # 2. 다음 재귀함수를 호출한다 (뽑은 카드가 1개 추가되었다)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()

    # 같은 방식을 반복문으로 들어간다면
    for num in range(3):
        path.append(num)
        recur(cnt + 1)
        path.pop()


# 돌아왔을 때 뽑아줘야

# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0)





