# # list(input() )
import sys

nlist =[]


try:
    while True:
        temp = input()
        nlist.append(temp)
except EOFError:
    print("끝")
print(nlist)

# a = sys.stdin.readlines()
# print(a)
# temp = input()
# print(temp)
# print(type(temp))

print(len(nlist))