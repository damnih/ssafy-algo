# 처음은 문자의 총 수
# 아니 근데 뒤에서 문자로 받아줘야 하는 거 아님? 

# 흐음...

lit_N, long_pw = input().split()
N = int(lit_N)
# 이렇게 받으면 pw는 문자열로 내비둬질까?? 

# 근데 중복임을 어케검출할수잇지 
# 흐음...... ... ...
for char in long_pw:

for i in range(1, N):
    if long_pw[i-1] == long_pw[i]:
        left_pw = long_pw[:i]
        right_pw = long_pw[i:]

# while 

