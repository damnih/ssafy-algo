# 16진수 문자로 이루어진 1차 배열
# 왼쪽부터 순차적으로 암호비트패턴을 찾아 차례대로 출력
# 암호는 연속됨


# 이거 그냥 암호도 거꾸로 받지?
password = {
    0: '001101',
    1: '010011',
    2: '111011',
    3: '110001',
    4: '100011',
    5: '110111',
    6: '001011',
    7: '111101',
    8: '011001',
    9: '101111',
}

re_pw = {}
for i in range(10):
    bin_pw = password[i]
    re_bin_pw = bin_pw[::-1]
    # print(re_bin_pw) # 잘됨!!!
    re_pw[i] = re_bin_pw

# print(re_pw) # 웅진짜잘됨

ans_re_pw = {}
for key, value in re_pw.items():
    ans_re_pw[value] = str(key)



# 배열을 받아 16 -> 10 -> 2 전환 패턴을 확인
T = int(input())
for tc in range(1, T+1):
    input_char = input()

    full_pattern = ''
    for char in input_char:
        dec_chg = int(char, 16)
        bin_chg = format(dec_chg,'04b')
        # print(bin_chg)
        full_pattern += bin_chg

    # print(full_pattern)
    # 그럼 이제 여기서 암호를 찾아주면 됨
    # 거꾸로!!! 거꾸로 찾으면 빠를 거 같은데 문자열을 뒤집을수있을까??
    re_pattern = full_pattern[::-1]
    # print(re_pattern)
    # 응 된다!!!!!!
    # 그렇다면 이제부터 거꾸로 돌린거를 보고 순회를 해서 1을 검출하면 잘라줄거얌!!!!!!!

    # re_pattern에 대해,,,
    # 앞에서부터 순회를 돌면서 1이면 멈추고 거기서부터 6자리씩 조회를 해주자

    pw_start = 0
    for char_num in re_pattern:
        if char_num == "1":
            break
        pw_start += 1
    # print(pw_start) # 잘 나옴

    # 이거 반복문의 끝이 언제 날지 모르잖아. 와일이다!!!!
    decode_list = []
    pw_flag = True
    while pw_flag:
        if pw_start <= len(re_pattern) - 6:
            seg_pw = re_pattern[pw_start : pw_start + 6]
            if ans_re_pw[seg_pw]: # 만약 이 키값이 존재한다면!!!!!!
                # 여기서 오류가 났던게, 0은 False처리가 되어서였거든
                # 그래서 그냥 딕셔너리에 아예 문자열로 넣어줘버림 ㅇㅇㅇㅇ!!!
                decode_list.append(ans_re_pw[seg_pw])
                pw_start += 6
            else:
                pw_flag = False
        else:
            pw_flag = False

    # print(decode_list) # 잘나옴!!

    # 그럼 이제 이걸 뒤집어서 출력해주기만 하면 됨!!!!!
    # 리스트니깐 그냥 슬라이싱 ^^!

    ans_decode = decode_list[::-1]

    # tc = 1
    # 얘를 의도에 맞게 바꿔주자 내용물은 다 스트링이니깐 스트링으로 넣어줘도 ㄱㅊ아
    ans = " ".join(ans_decode)
    print(f"#{tc} {ans}")
