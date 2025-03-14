# 주사위 3개를 던져 합이 10 이하인 경우는 몇 개인가??
# 종료조건: 3번 던진다

path = []
result = 0

def recur(cnt, total):
    global result

    if cnt == 3:
        # # 근데 합이 10 이하가 몇개인지 보고시픔
        # # if path의 합이 10 이하라면..
        # if sum(path) < = 10:
        #     result += 1
        #     print(path)
        # return
    # 근데 이런 경우 sum하는 만큼 path의 길이만큼 반복되기 때문에 비효율적 O(N)!!!
    # 이 sum을.. 주사위 던질 때마다 해줄 수는 없나?
    # 재귀함수의 인자로 받고 늘려주면 되겠다
        if total <= 10:
            result += 1
            print(path)

    for num in range(1, 7):
        path.append(num)
        # 주사위 결과를 더해서 전달
        recur(cnt + 1, total + num)
        path.pop()