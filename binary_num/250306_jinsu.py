hex_str = 'F9A3'
bin_str = ''

for char in hex_str:
    decimal_num = int(char, 16) # 16진수를 10진수로 변환해주는거
    bin_str += format(decimal_num, '04b')  # (ex. '0'->'0000') # 2진수로 바꿔줌

print(bin_str)  # 1111100110100011

# binary를 안 쓰는 이유 : 결과에 접두어가 붙음, 그래서 불편함

# 포맷의 두번째 인자를 활용해서 진수를 결정
# b는 바이너리
# x 는 헥사 16진수 소문자로 표현
# X 는 헥사 16진수 대문자로 표현
#
#
# 0b 라는 이진수임을 알려주는 접두어임
#
# binary = 2진수
# heximal = 16진수
# octamal = 10진수
#
# 오늘 기억해야 할 것은 int와 포맷
#
# 내장함수로 먼저 편하게 풀이
# 그다음에 내장함수를 안 쓴 방법으로 풀이



