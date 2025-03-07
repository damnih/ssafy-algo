# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7비트씩 묶어 십진수로 변환 



# 16진수 문자열을 판단
# 그 문자열을 각각 2진수로 변환 
# ( 16진수이므로 최대길이 4가 될테니 4의자리로 고정시키자)
# 이 28자리(유동,  처음 문자열이 어떻게 주어지는지가 중요)에 대해서, 
# 7자리씩 슬라이싱.
# 7자리 다 안채워지면 그대로 냅두고 계산 


# 01D0 6079 
# 0000 0001 13=1101 0000 0110 0000 0111 1001

# 0000000 0 
# 1110100 4 16 32 64 116  
# 0001100
# 0000111
# 1001

# 엥 에반데 내가 이해한게 아닌데???


# 아 아래 문제조건 지금봄
# “문제 조건이 명확하지 않으니 아래 조건을 추가해서 작성해주세요.”

# 만약 자른 7비트가 '0000000'이면, 실제로는 '0000'(앞 4비트)만 버리고
# 뒤에 남은 3비트('000')는 다음 chunk와 합쳐서 진행하기

# 0000 0001 13=1101 0000 0110 0000 0111 1001
# 이게 사실상 
# 0001110 14
# 1000001 65
# 1000000 64 
# 1111001 64 32 16 8 1 8*15+1 121
# 이라는거네 

# 웅웅 이해했어~~~~~~~~~~~

# 만약 자른 7비트가 0000000이면,, 이게 좀 어려운 부분분이 되겠다 ㅎ ㅜㅜ 


def make_seven(bin_char):
    i = 0
    seven_bin_list = []
    while i < len(bin_char):
        k = 0
        seven_bin_char = ""

        while k < 7 and i < len(bin_char):
            if i + k < len(bin_char):
                seven_bin_char += bin_char[i + k]
                # print(seven_bin_char)
                if seven_bin_char == "0000000":
                    i = i + k - 2
                    break
                # i += 1
                else:
                    # seven_bin_list.append(seven_bin_char)
                    k += 1
            else:
                # seven_bin_list.append(seven_bin_char)
                i = len(bin_char)
        # seven_bin_list.append(seven_bin_char)
        # i += 7
        else:
            seven_bin_list.append(seven_bin_char)
            i += 7
    return seven_bin_list


T = int(input())

for tc in range(1, T+1):
    hexa_arr = input()
    dec_list = []
    # 16진수 문자열을 판단
    # 그 문자열을 각각 2진수로 변환
    # how? 16-> 10-> 2의 과정을 거침
    for char in hexa_arr:
        # 일단 10진수 변환
        dec_changed = int(char, 16)
        dec_list.append(dec_changed)

    # 일단 2진수 모아둘 문자열을 생각하고
    bin_char = ""
    # 이 10진수들에 대해서 2진수 변환 ㄱㄱ
    # ( 16진수이므로 최대길이 4가 될테니 4의자리로 고정시키자)
    for dec_changed in dec_list:
        bin_changed = format(dec_changed, '04b')
        # # 항상 0으로 채울지말지여부/자릿수/몇진수인지 순서임임
        bin_char += str(bin_changed)

    seven_bin_list = make_seven(bin_char)
    ans_dec_nums = []

    for seven_bins in seven_bin_list:
        dec_num = int(seven_bins, 2)
        ans_dec_nums.append(dec_num)

    # print(ans_dec_nums)  # 잘 나왔어!!!!
    print(f"#{tc}", *ans_dec_nums)

'''
hexa_arr = input()
# hexa_arr = '0F97A3'
# hexa_arr = '003F'

# 십진수로 만들어주는건 int
# 다른진수로 만들어주는건 format

# print(int('F', 'h'))
print(int('F', 16)) # 웅 이거 잘맞아~~!!!

dec_list = []
# 16진수 문자열을 판단
# 그 문자열을 각각 2진수로 변환
# how? 16-> 10-> 2의 과정을 거침
for char in hexa_arr:
    # 일단 10진수 변환
    dec_changed = int(char, 16)
    dec_list.append(dec_changed)

# 일단 2진수 모아둘 문자열을 생각하고
bin_char = ""

# 이 10진수들에 대해서 2진수 변환 ㄱㄱ
# ( 16진수이므로 최대길이 4가 될테니 4의자리로 고정시키자)
for dec_changed in dec_list:
    bin_changed = format(dec_changed, '04b')
    # # 항상 0으로 채울지말지여부/자릿수/몇진수인지 순서임임
    bin_char += str(bin_changed)

print(bin_char) # 잘 나옴!!!!!

# bin_char = '00000001010111100000000000000011'
          # 0000 0001 0101 1110 0000 0000 0000 0011
          # 0000000 1010111 1000000 0000000 0011
          # 0000 0001010 1111000 0000 0000 000011
# 그렇다면 이 0과 1로 이루어진 문자열에 대해서 .. 
# 7자리씩 슬라이싱.
# 7자리 다 안채워지면 그대로 냅두고 계산 
# 만약 7자리가 전부 0이라면 '0000000' 4자리 버리고 000붙여서 뒤에 이어지는 것과 연동하기 
# 즉 0000000 임을 확인하면,, 인덱스 4를 0으로 바꾸고 쭉 이어준다 

# i = 7 * i # 0


def make_seven(bin_char):
    i = 0
    seven_bin_list = []
    while i < len(bin_char):
        k = 0
        seven_bin_char = ""
        
        while k < 7 and i < len(bin_char):
            if i + k < len(bin_char):
                seven_bin_char += bin_char[i + k]
                # print(seven_bin_char)
                if seven_bin_char == "0000000":
                    i = i + k - 2
                    break
                # i += 1
                else:
                    # seven_bin_list.append(seven_bin_char)
                    k += 1
            else:
                # seven_bin_list.append(seven_bin_char)
                i = len(bin_char)
        # seven_bin_list.append(seven_bin_char)
        # i += 7
        else:
            seven_bin_list.append(seven_bin_char)
            i += 7
    return seven_bin_list

seven_bin_list = make_seven(bin_char)
print(seven_bin_list)

ans_dec_nums = []

for seven_bins in seven_bin_list:
    dec_num = int(seven_bins, 2)
    ans_dec_nums.append(dec_num)

print(ans_dec_nums) # 잘 나왔어!!!!
# .. 하... 이제...... 또 출력의 늪에 빠짐...
tc = 1
print(f"#{tc}", *ans_dec_nums)

# result.append(int(num, 2))
# print(f"#{tc}", *result)

'''