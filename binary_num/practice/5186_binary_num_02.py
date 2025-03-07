
'''
# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 함
0.625를 이진수로 바꾸면
0.101

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인
이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
13자리 이상이 필요한 경우에는 ‘overflow’를 출력
'''

# 이분의일 사분의일 팔분의일 십육분의일 삼십이분의일 등등등... 더해서,, 그 이진수가 나오기,,

# 이거 일단 순차적으로 빼주면서 들어가야 할 거 같은데?

# 기본 수랑, 2의 마이너스 엔승 크기를 비교함
# 기본 수가 2의 마이너스 엔승보다 크다면, -> 이의 마이너스 엔승을 빼줌. 그것이 다시 기본수가 됨
# 작다면-> 엔+1
# 이 바뀐 엔으로
# 기본 수랑 2의 마이너스 엔승 크기를 비교
#
# 여기를 계속 반복하는거 ㅇㅇ
#
# 12자리까지 ok랬으니깐~~~




def binary_make_twelve(N):

    def make_ans(b_list):
        ans = ""
        for char in b_list:
            ans += str(char)
        return ans

    # 이진수를 담을 빈 배열
    binary_chart = []
    # 12자리까지만 갈거니깐~~~
    for i in range(1, 13):
        if N > 2 ** (-i):
            N -= 2 ** (-i)
            binary_chart.append(1)
        elif N == 2 ** (-i):
            binary_chart.append(1)
            break
        else:
            binary_chart.append(0)
    # 그니깐 이러고나면 N의 잔여물이 남는 상황인거잖아?
    # 2의 마이너스 12승 보다 작은게 잔여물로 남는 상황이겠지?
    # 그렇다면 N의 크기로 결정하면 되겠다
    if N < 2 ** (-12):
        # raise "overflow"
        return "overflow"
    else:
        ans = make_ans(binary_chart)
        return ans

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = binary_make_twelve(N)
    print(f"#{tc} {ans}")


# else:

# print(binary_chart)


'''

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    binary_chart = []

    for i in range(1, 13):
        if N > 2 ** (-i):
            N -= 2 ** (-i)
            binary_chart.append(1)
        elif N == 2 ** (-i):
            binary_chart.append(1)
            break
        else:
            binary_chart.append(0)

    # 그니깐 이러고나면 N의 잔여물이 남는 상황인거잖아?
    # 2의 마이너스 12승 보다 작은게 잔여물로 남는 상황이겠지?
    # 그렇다면 N의 크기로 결정하면 되겠다

    if N < 2 ** (-12):
        # raise "overflow"
        print(f"#{tc} overflow")
    else:
        ans = make_ans(binary_chart)
        print(f"#{tc} {ans}")

'''


'''

N = float(input())

binary_chart = []

# i = 1
# while i < 13:
#     if N > 2 ** (-i):
#         N -= 2 ** (-i)
#         binary_chart.append(1)
#         i += 1
#     elif N == 2 ** (-i):
#         binary_chart.append(1)
#         break
#     else:
#         binary_chart.append(0)
#         i += 1

for i in range(1, 13):
    if N > 2 ** (-i):
        N -= 2 ** (-i)
        binary_chart.append(1)
    elif N == 2 ** (-i):
        binary_chart.append(1)
        break
    else:
        binary_chart.append(0)

# 그니깐 이러고나면 N의 잔여물이 남는 상황인거잖아?
# 2의 마이너스 12승 보다 작은게 잔여물로 남는 상황이겠지?
# 그렇다면 N의 크기로 결정하면 되겠다

if N < 2 ** (-12):
    # raise "overflow"
    print("overflow")
else:
    ans = make_ans(binary_chart)
    print(ans)
'''