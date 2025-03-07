target = 74

def dec_to_binary(target):
    binary_num = ""

    while target > 0:
        # 2로 계속 나누면서 나머지가 1이 될 때까지 반복한다
        remain = target % 2 # 2로 나눈 나머지
        binary_num = str(remain) + binary_num # 문자열은 그냥 그대로 앞에 더해지지!!!
        target = target // 2
        # 근데 저렇게 해도 돼?? 아 binary num 으로는 연산을 안하니깐 ㄱㅊ
    print(binary_num)

dec_to_binary(target)

def binary_to_decimal(binary_str):

    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_number += 2 ** pow # 현재 지수를 올려줌
            pow += 1 # 곱해줬으니 다음 연산을 위해 지수를 올려줌
        else:
            pow += 1

    print(decimal_number)

binary_to_decimal()

def decimal_to_hexadecimal(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16

    print(hex_number)

decimal_to_hexadecimal(256)