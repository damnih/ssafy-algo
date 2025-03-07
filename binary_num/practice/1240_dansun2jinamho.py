# 1. 암호코드는 8개의 숫자로 이루어져 있다.
#
# 2. 암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.
#    ※ 길이가 56가 아닌 코드는 주어지지 않는다. 주어진 암호코드는 주어진 규칙대로 해독할 수 있음을 보장한다.
#       암호코드의 각 숫자가 암호화되는 규칙은 주어진 그림1을 참고하라.
#
# 3. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.
#     ex) 암호코드가 88012346일 경우,
#     ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.
#     ex) 암호코드가 19960409일 경우,
#     ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다.


# 이거 7개씩 긁으면서,,
# 기존에 있던 것과 같으면 카운트를 늘리다가 값이 다르면 그 때 카운트를 초기화하고 새로 써주는 식으로 넣어서
# 3211 1231 이런거로 구분해서 숫자 조회하면 편할거같긴 한데,,
#
# 해볼까??
# "01110110110001011101101100010110001000110100100110111011"

# 7개씩 잘라

# sample_amho = '0111011'
# sample_amho = "1011100"

from pprint import pprint

# 7자리 배열을 10진수의 숫자로 변환
num_dict = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

# print(num_dict['[3, 1, 1, 2]']) # 된당

# print(sample_amho[1])

# 스트링이라서 이렇게 슬라이싱 해서 뽑아낼 수 있다 ㅇㅇㅇ

def what_dec_num_key(sample_amho):
    johoi_arr = []
    num = 1
    i = 1
    while i < len(sample_amho):
        # 만약 이전자리와 지금자리가 다르다면, num을 초기화해줌
        if sample_amho[i-1] != sample_amho[i]:
            # if i == 1: # 근데 처음자리와 둘째자리가 다르다면? 일단 처음자리에 1 넣어줘야됨
            #     johoi_arr.append(1)
            johoi_arr.append(num)
            num = 1
            i += 1
        # 만약 이전자리와 지금자리가 같다면,, 그냥 num을 올려줌
        else:
            num += 1
            i += 1
    johoi_arr.append(num)
    key = tuple(johoi_arr)
    return key

# 헐 잘나와 굿굿
# 리스트는 가변이니깐 불변인 튜플로 바꿔줄까??
# 아냐.. 불안해.. 귀찮아.. 할거나 먼저 해보자....
# 헐 딕셔너리 키로 튜플은 사용 가능해
# 그냥 바로 변환을 해주면 되는거였어!!!!!!

#
# four = "0100011"
#
# guess = what_dec_num_key(four)
# # qwe = tuple(guess)
# # print(qwe)
# print(num_dict[guess])
# # print(num_dict[qwe])
# print(type(num_dict[guess])) # int

# print(johoi_arr)

# # ## 이 위에까지 있는 정보는 7자리 암호를 읽으면 바로 숫자로 변환하는 과정임


''''''
# 이거 일단,, 1로 시작하는 순간부터 암호임을 인식할 수 있다,,
# 이거 나중에 해결하자
# 아 이거 무조건 숫자는 1로 끝나네
# 암호면 56번째 배열이 무조건 1인거야 ㅇㅋㅇㅋ
''''''

# 일단 출력을 ㅈㄴ 길게 받잖아
# 여기서 1이 있는지 여부를 확인해
# 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데
# 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).
N, M = map(int, input().split())

matrix = [input() for _ in range(N)]
pprint(matrix)

def find_endpoint(matrix, N, M):
    for i in range(N):
        for j in range(M, -1, -1):
            if matrix[i][j] == '1':
                end_i = i
                end_j = j
                return end_i, end_j

end_i, end_j = find_endpoint(matrix, N, M)
mai_list = matrix[end_i][end_j - 55 : end_j + 1]

print(mai_list)

# seven_amho = "0111011"
#
# key = what_dec_num_key(seven_amho)
# num = num_dict[key] # 여기까진 int
# str_num = str(num)

# 이제 이 반환한 num 들을 문자 취급해 계속 더해줘야하는거임 어디로? 8자리 잇는것으로
# main_list = "01110110110001011101101100010110001000110100100110111011"
main_list = "00110010100011010001101011110110111001001100100110111011"
eight_num = ""
for i in range(8):
    seven_amho = main_list[7 * i : 7 * (i + 1)]
    print(seven_amho)
    key = what_dec_num_key(seven_amho)
    num = num_dict[key]  # 여기까진 int
    str_num = str(num)
    eight_num += str_num

print(eight_num) # 잘나옴 75755027

# 그렇다면 이 eight_num에 대해서,, 문자열이니깐
# 홀수번째 짝수번째에 대해서 암호인지 확인을 해줘야함

hol = 0
jjak = 0

for j in range(4):
    hol += int(eight_num[2 * j])
    jjak += int(eight_num[2 * j + 1])

print(hol) # 21 7 7 5 2 # 잘나옴
print(jjak) # 17 5 5 0 7 # 잘나옴

def whether_crypto(hol, jjak):
    if (hol * 3 + jjak) % 10 == 0:
        return hol + jjak
    else:
        return 0

# 헐 완성했네?
print(whether_crypto(hol, jjak)) # 잘됨



'''
이거 나눠서 조회하는거 

johoi_arr = []

num = 1
i = 1
while i < len(sample_amho):
    # 만약 이전자리와 지금자리가 다르다면, num을 초기화해줌
    if sample_amho[i-1] != sample_amho[i]:
        # if i == 1: # 근데 처음자리와 둘째자리가 다르다면? 일단 처음자리에 1 넣어줘야됨
        #     johoi_arr.append(1)
        johoi_arr.append(num)
        num = 1
        i += 1
    # 만약 이전자리와 지금자리가 같다면,, 그냥 num을 올려줌
    else:
        num += 1
        i += 1
johoi_arr.append(num)
'''