
# level 주사위 3개를 던졌을 떄 
# branch 가지가 몇개인지 

N = 3
path = []

def recur(cnt):
    if cnt == N:
        print(path)
        return 
    
    for i in range(1, 7):
        path.append(i)
        recur(cnt+1)
        path.pop()


recur(0)


def no_re_recur(cnt, start):
    if cnt == N:
        print(path)
        return 
    
    for i in range(start, 7):
        path.append(i)
        no_re_recur(cnt+1, i+1)
        path.pop()

recur(0, 1)



def yes_re_recur(cnt, start):
    if cnt == N:
        print(path)
        return 
    
    for i in range(start, 7):
        path.append(i)
        yes_re_recur(cnt+1, i)
        path.pop()

recur(0, 1)


# 중복을 없애거나 같이 쓰거나 ㅇㅇ!! 

