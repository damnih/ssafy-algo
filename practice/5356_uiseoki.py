# 글자 다섯개씩 만들었으니깐 

# blackboard = [list(input().split()) for _ in range(5)]

# print(blackboard) # 웅 잘됨 

T = int(input())

for tc in range(1, T+1):
    blackboard = [list(input()) for _ in range(5)]

    print(blackboard)
# def vertical_bb(list):
    len_list = []
    for i in range(5):
        word_length = len(blackboard[i])
        len_list.append(word_length)
    max_length = max(len_list)

    vertical = []

    for j in range(max_length):
        for i in range(5):
            # if blackboard[i][j] == True: # 아냐 이러면 0도 false처리돼 
            # 그냥 델타탐색 벽처리를 해주자... 
            if 0 <= j < len_list[i] : 
                vertical.append(blackboard[i][j])
            else:
                continue 
    print(vertical)
    ans = "".join(vertical)
    print(f"#{tc} {ans}")


'''
def vertical_bb(list):
    len_list = []
    for i in range(5):
        word_length = len(list[i])
        len_list.append(word_length)
    max_length = max(len_list)

    vertical = []

    for j in range(max_length):
        for i in range(5):
            # if blackboard[i][j] == True: # 아냐 이러면 0도 false처리돼 
            # 그냥 델타탐색 벽처리를 해주자... 
            if 0 <= j < len_list[i] : 
                vertical.append(list[i][j])
            else:
                continue 
    return vertical 
'''



# T = int(input())

# for tc in range(1, T+1):
#     blackboard = [list(input().split()) for _ in range(5)]
#     vetical_word = vertical_bb(blackboard)
#     ans = "".join(vetical_word)
#     print(f"#{tc} {ans}")






# print(vertical) # 엉 잘나옴 

# ans = "".join(vertical)

