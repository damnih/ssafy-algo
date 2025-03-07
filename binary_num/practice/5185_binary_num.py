# N자리의 16진수가 주어지면 각 자리수를 4자리 2진수로 표시하는 프로그램을 만드시오
# 단 2진수의 앞자리 0도 반드시 출력한다
#
#
# 일단,,

hex_dict= {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

# hex_dict['0'] = 0


# print(int('F', 16))


# N자리 문자열을 받아서 앞에서부터 순회를 돌아줌
# 순회해서 빠져나온 그건 16진수이므로 10진수로 변환한 뒤 그걸 다시 2진수로 변환

T = int(input())

for tc in range(1, T+1):
    str_N, input_num = input().split()
    N = int(str_N)
    # 나는,, 아직도,, 쉽게 답을 이어붙이는 방법을 모른다,,,
    # 아는 방법은 문자열로 만들어 이어붙이는 방법 뿐,,
    ans = ""
    for char in input_num:
        dec_num = int(char, 16)
        # 이 십진수를 2진수로 변경
        # format 함수 쓰면 쉽더라~~~
        bin_num = format(dec_num, '04b')
        str_bin_num = str(bin_num)
        ans += bin_num

    print(f"#{tc} {ans}")






# # num = 7
# asd = 'A'
# num = float(asd)
# aa = format(num, '04b')
#
# print(aa)


