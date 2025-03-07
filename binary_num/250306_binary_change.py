# 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기
#
# 0000001 0001101
#
# 얘를 문자열로 받아들여서
# 7번 순회를 뒤에서부터 돌리는데,
# 그 i번째에 나온 문자가 1이라면, 2**i를 더해주고
# i번째에 나온 문자가 0이라면, 0을 더해줌
#
# 7개씩 묶으라고 한 건
# 입력문을 7개씩 묶으라고 한 이야기
#
# 인풋은 길게 나오고 이걸
#
# 스트링에 팝 쓸 수 있나??
#
#
# 아니 문자열을 7개씩 슬라이싱하는거
# 지금 이게 제일 문제야 ㅁㅊ
#
# 나머지는 걍 int 쓰면 될거같단말이지??
#
# input 받아와.. 이 문자열을... 7개씩 잘라서.. 새로운 문자열로 만들어,,


# first_input = input() # 이러면 문자열로 들어옴
#
# churi_num = ""
#
# while
#
#
#
#
#
#
# for char in seven_char:

exstr = "012345678901234567890123456789012345678901"

# 0123456
# 7890123
# 4567890
# 1234567
# 8901234
# 5678901

# doina = exstr[:7]

# print(doina)

# 스트링도 시퀀스이기때문에
# 시퀀스에서 쓸 수 있는건 전부 쓸 수 있는 거임

# len(exstr)

# 7개씩 쪼개는 함수
# 반복해서 7개씩 자를 거라 i를 같이 받아줌
def make_seven(exstr, i):
    # i = 0
    if i <= len(exstr) // 7:
        # n = 7 + 7 * i
        # 문자열은 시퀀스이기때문에 리스트처럼 자르기 가능
        strcase = exstr[7 * i : 7 * (i + 1)]
    return strcase

# ans = make_seven(exstr, 5)

# print(ans)
T = int(input())

for tc in range(1, T+1):
    exstr = input()
    ans = ""
    for i in range(len(exstr) // 7):
        state = make_seven(exstr, i)
        ans_part = str(int(state, 2))
        ans_blank = " "
        ans += ans_part
        ans += ans_blank

    print(f"#{tc} {ans}")

