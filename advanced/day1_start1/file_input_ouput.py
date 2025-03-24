import sys
# stdin: standard input (표준 입력)
#   open("input.txt", "r")
#       input.txt file 을 읽기 모드로 열겠다.
#       "r" : 읽기 모드
# 테스트케이스를 수정하면서
#   디버깅이 가능하다!
sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

a, b = map(int, input().split())
print(a, b)
