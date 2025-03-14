# 베이비진 검사
# 숫자 3개가 연속되었는가
# 숫자 3개가 같은가

# 6자리 숫자를 입력
# - 모든 순서를 보아야 한다 (순열)
'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

used =[0] * 6 # 0으로 해도 false로 해도 다 ㄱㅊ
path = []
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2 이 되면 베이비진인거임

    # 앞 세자리 확인해주고
    a, b, c = path[0], path[1], path[3]
    if a == b == c: # triplet
        cnt += 1
    elif a == (b-1) == (c-2): # run
        cnt += 1

    # 뒤 세자리 확인해주면 됨

def recur(cnt):
    if cnt == 6:
        # baby-gin인지 검사
        if is_baby_gin():
            baby_gin_result = True

        return

    for idx in range(6):
        # 인덱스를 이미 썼다면, 뽑지 말아라,, 이렇게 가야할거같음 자라하나하나 검출하는 거니깐
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0


print('YES' if baby_gin_result else 'NO')