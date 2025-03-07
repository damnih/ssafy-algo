
import sys
sys.stdin = open("1240_input.txt", "r")


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
    return tuple(johoi_arr)

# 암호문 어디에 있는지 딱 그 좌표만 찾아주는 함수 (리스트 슬라이싱 따로 해야됨)
# 일단 출력을 길게 받잖아
# 여기서 1이 있는지 여부를 확인해
# 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데
# 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).
def find_endpoint(matrix, N, M):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if matrix[i][j] == '1':
                end_i = i
                end_j = j
                return end_i, end_j

# 암호 맞는지 확인하기 위한 함수
# 홀*3 + 짝 이 10의 배수이면 암호맞음 아니면 0출력
def whether_crypto(hol, jjak):
    if (hol * 3 + jjak) % 10 == 0:
        return hol + jjak
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    end_i, end_j = find_endpoint(matrix, N, M)

    # 딱 암호문이 있는 위치만 잘라줌
    crypto_list = matrix[end_i][end_j - 55 : end_j + 1]

    # 이 crypto_list를 통해 암호가 맞는지 확인하고, 암호를 해독할거임
    eight_num = ""
    for i in range(8):
        seven_amho = crypto_list[7 * i : 7 * (i + 1)]
        # print(seven_amho)
        key = what_dec_num_key(seven_amho)
        num = num_dict[key]  # 여기까진 int
        # 이제 이 반환한 num 들을 문자 취급해 계속 더해줘야하는거임 8자리 잇는것으로 완성되게
        str_num = str(num)
        eight_num += str_num

    # 그렇다면 이 eight_num에 대해서,, 문자열이니깐
    # 홀수번째 짝수번째에 대해서 암호인지 확인을 해줘야함
    hol = 0
    jjak = 0
    for j in range(4):
        hol += int(eight_num[2 * j])
        jjak += int(eight_num[2 * j + 1])

    ans = whether_crypto(hol, jjak)

    print(f"#{tc} {ans}")



