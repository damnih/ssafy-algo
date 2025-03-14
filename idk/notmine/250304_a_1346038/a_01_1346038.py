


#
# for i in range ,,로 가느냐
# while로 가느냐,,,


#
# day = 1
#
# day % 2 == 1: #홀수날
# day % 2 == 0: #짝수날

'''
5
2 
5 5
2 
4 2
2 
3 4
4 
2 3 10 5
4
1 2 3 4
'''

'''

#1 0

#2 2

#3 1

#4 14

#5 4
'''


# day += 1

# 이거 그냥 솔직히 한 나무 조지고
# 다음 나무로 넘어가면 될 거 같은데?
# 하루에 나무 하나에밖에 못준다잖아
#
# 그리고 그 조지는 나무의 길이가 최댓값이랑 2 차이나는데, 홀수날일때에,
# 그 물은 바로 다음 나무에 주고
# 짝수날 됐을 떄 원래 나무에 주는 식으로만, 예외처리를 해주면 될 거 같애~!

# N = int(input())
# tree = list(map(int, input().split()))
#
# # print(tree)
#
# max_tree = max(tree)
# # max_idx = tree.index(max_tree)
#
# # 아니다 그냥 인덱스 증가시켜 가면서,, 하면 되지 않나??
# # 그렇네 i = N 에 도달하면 반복문 종료!!! 하면 되네
# # i = N - 1 까지는 처리를 해줘야하니깐 ㅇㅇㅇㅇ
#
# # 아니다 내가 해야하는 건 어차피 나무들의 키를 맞출 날짜밖에 없으니깐,,
# # 이거 그냥 내림차순해서 오른쪽으로 갈수록 키가 작으면 편하겠네
# # 일단 불안하니깐 원본 복제해주고
# sorted_tree = tree[:]
# # 정렬
# sorted_tree.sort(reverse=True)
# # print(sorted_tree) # 오케이 잘돼



def find_min_days(sorted_tree, max_tree):
    i = 0
    day = 1

    while i < N:
        if sorted_tree[i] != max_tree:
            # print(f"현재 위치 i={i}, 지금의 날짜는 day{day} {sorted_tree}아직 물주기 전이야 이 홀짝에 맞춰서 와일문 맨끝에서 바뀔거야,,")
            # 이제 날짜의 홀짝 검출해야돼
            if day % 2 == 1:  # 홀수날
                # sorted_tree[i] += 1 # 이게 기본 로직, 모든 예외가 아닐 때 이거 그냥 무작위로 넣으면 됨
                # 예외) 근데 만약 두 칸 차이라면?
                if max_tree - sorted_tree[i] == 1:
                    sorted_tree[i] += 1
                    day += 1
                    i += 1
                elif max_tree - sorted_tree[i] == 2:
                    # 옆자리로 옮겨줘 얘는 옆이 마찬가지로 2 차이나도 ㄱㅊ아 내가 2먹고 옆은 1+1 하면 깔끔하니깐 ㅇㅇ
                    # 옆자리의 인덱스를 조회해야돼
                    if i + 1 < N:  # 옆자리가 인덱스 안에 있다면, 걔에게 물을 줌
                        sorted_tree[i + 1] += 1  # 물 주고
                        day += 1  # 날짜 주고
                        # 인덱스만 낫증가
                    else:  # 옆자리에 인덱스가 없다면
                        day += 1
                        # 물 안줌 = 인덱스는 낫 증가, 나무 낫 증가, 날짜만 증가
                else:  # 이 예외에 해당 안한다면?
                    # 그냥 물줘라
                    sorted_tree[i] += 1
                    day += 1
                    # 꽉 차기 전까지는 i 증가 ㄴㄴ
                    # i += 1
                # print(f"홀수날 증가확인 {sorted_tree}")
            else:  # day % 2 == 0: 짝수날
                # 예외) 만약 이 인덱스에 해당하는 놈이 한 칸 차이난다면?
                if max_tree - sorted_tree[i] == 2:
                    sorted_tree[i] += 2
                    day += 1
                    i += 1
                elif max_tree - sorted_tree[i] == 1:
                    # 옆자리로 옮겨줘
                    # 근데 이건 이제 1보다 더 큰 차이가 날 때까지 옆자리로 옮겨줘야 하는거지
                    k = 0
                    while k < N - i:
                        k += 1
                        if sorted_tree[i + k] != max_tree - 1:
                            break
                    # 이 때의 k로 인덱스 조회를 해주면 됨
                    sorted_tree[i + k] += 2  # 물 주는거야
                    day += 1
                    # 근데 옆자리에 물 준 거니깐 인덱스는 증가 안해
                # 예외가 아닌 나머지들은 전부 그냥 물줘
                else:
                    sorted_tree[i] += 2
                    day += 1
                    # 꽉 차기 전까지는 i증가 ㄴㄴ
                    # i += 1
                # print(f"짝수날 증가확인 {sorted_tree}")
        else:  # sorted_tree[i] == max_tree:
            i += 1  # 다음 인덱스로 가라
        # print(f"현재 위치 i={i - 1}, 지금의 날짜는 day{day - 1} {sorted_tree} 여기선 물줬어 ")
    return day




'''
잘 돌아가는 거임 제한시간 초과가 났을 뿐,, 이거 백업 

def find_min_days(sorted_tree, max_tree):
    i = 0
    day = 1

    while i < N:
        if sorted_tree[i] != max_tree:
            # print(f"현재 위치 i={i}, 지금의 날짜는 day{day} {sorted_tree}아직 물주기 전이야 이 홀짝에 맞춰서 와일문 맨끝에서 바뀔거야,,")
            # 이제 날짜의 홀짝 검출해야돼
            if day % 2 == 1:  # 홀수날
                # sorted_tree[i] += 1 # 이게 기본 로직, 모든 예외가 아닐 때 이거 그냥 무작위로 넣으면 됨
                # 예외) 근데 만약 두 칸 차이라면?
                if max_tree - sorted_tree[i] == 2:
                    # 옆자리로 옮겨줘 얘는 옆이 마찬가지로 2 차이나도 ㄱㅊ아 내가 2먹고 옆은 1+1 하면 깔끔하니깐 ㅇㅇ
                    # 옆자리의 인덱스를 조회해야돼
                    if i + 1 < N:  # 옆자리가 인덱스 안에 있다면, 걔에게 물을 줌
                        sorted_tree[i + 1] += 1  # 물 주고
                        day += 1  # 날짜 주고
                        # 인덱스만 낫증가
                    else:  # 옆자리에 인덱스가 없다면
                        day += 1
                        # 물 안줌 = 인덱스는 낫 증가, 나무 낫 증가, 날짜만 증가
                else:  # 이 예외에 해당 안한다면?
                    # 그냥 물줘라
                    sorted_tree[i] += 1
                    day += 1
                    # 꽉 차기 전까지는 i 증가 ㄴㄴ
                    # i += 1
                # print(f"홀수날 증가확인 {sorted_tree}")
            else:  # day % 2 == 0: 짝수날
                # 예외) 만약 이 인덱스에 해당하는 놈이 한 칸 차이난다면?
                if max_tree - sorted_tree[i] == 1:
                    # 옆자리로 옮겨줘
                    # 근데 이건 이제 1보다 더 큰 차이가 날 때까지 옆자리로 옮겨줘야 하는거지
                    k = 0
                    while k < N - i:
                        k += 1
                        if sorted_tree[i + k] != max_tree - 1:
                            break
                    # 이 때의 k로 인덱스 조회를 해주면 됨
                    sorted_tree[i + k] += 2  # 물 주는거야
                    day += 1
                    # 근데 옆자리에 물 준 거니깐 인덱스는 증가 안해
                # 예외가 아닌 나머지들은 전부 그냥 물줘
                else:
                    sorted_tree[i] += 2
                    day += 1
                    # 꽉 차기 전까지는 i증가 ㄴㄴ
                    # i += 1
                # print(f"짝수날 증가확인 {sorted_tree}")
        else:  # sorted_tree[i] == max_tree:
            i += 1  # 다음 인덱스로 가라
        # print(f"현재 위치 i={i - 1}, 지금의 날짜는 day{day - 1} {sorted_tree} 여기선 물줬어 ")
    return day
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_tree = max(tree)
    # 내가 해야하는 건 어차피 나무들의 키를 맞출 날짜밖에 없으니깐,,
    # 이거 그냥 내림차순해서 오른쪽으로 갈수록 키가 작으면 편하겠네
    # 일단 불안하니깐 원본 복제해주고
    sorted_tree = tree[:]
    # 정렬
    sorted_tree.sort(reverse=True)

    ans = find_min_days(sorted_tree, max_tree) - 1
    print(f"#{tc} {ans}")




'''
여기 원본이야 ㄱㄱㄱ 

i = 0
day = 1

while i < N:
    if sorted_tree[i] != max_tree:
        print(f"현재 위치 i={i}, 지금의 날짜는 day{day} {sorted_tree}아직 물주기 전이야 이 홀짝에 맞춰서 와일문 맨끝에서 바뀔거야,,")
        # 이제 날짜의 홀짝 검출해야돼
        if day % 2 == 1: # 홀수날
            # sorted_tree[i] += 1 # 이게 기본 로직, 모든 예외가 아닐 때 이거 그냥 무작위로 넣으면 됨
            # 예외) 근데 만약 두 칸 차이라면?
            if max_tree - sorted_tree[i] == 2:
                # 옆자리로 옮겨줘 얘는 옆이 마찬가지로 2 차이나도 ㄱㅊ아 내가 2먹고 옆은 1+1 하면 깔끔하니깐 ㅇㅇ
                # 옆자리의 인덱스를 조회해야돼
                if i+1 < N: # 옆자리가 인덱스 안에 있다면, 걔에게 물을 줌
                    sorted_tree[i+1] += 1 # 물 주고
                    day += 1 # 날짜 주고
                    # 인덱스만 낫증가
                else: # 옆자리에 인덱스가 없다면
                    day += 1
                    # 물 안줌 = 인덱스는 낫 증가, 나무 낫 증가, 날짜만 증가
            else: # 이 예외에 해당 안한다면?
                # 그냥 물줘라
                sorted_tree[i] += 1
                day += 1
                # 꽉 차기 전까지는 i 증가 ㄴㄴ
                # i += 1
            print(f"홀수날 증가확인 {sorted_tree}")
        else: # day % 2 == 0: 짝수날
            # 예외) 만약 이 인덱스에 해당하는 놈이 한 칸 차이난다면?
            if max_tree - sorted_tree[i] == 1:
                # 옆자리로 옮겨줘
                # 근데 이건 이제 1보다 더 큰 차이가 날 때까지 옆자리로 옮겨줘야 하는거지
                k = 0
                while k < N - i:
                    k += 1
                    if sorted_tree[i + k] != max_tree - 1:
                        break
                # 이 때의 k로 인덱스 조회를 해주면 됨
                sorted_tree[i+k] += 2 # 물 주는거야
                day += 1
                # 근데 옆자리에 물 준 거니깐 인덱스는 증가 안해
            # 예외가 아닌 나머지들은 전부 그냥 물줘
            else:
                sorted_tree[i] += 2
                day += 1
                # 꽉 차기 전까지는 i증가 ㄴㄴ
                # i += 1
            print(f"짝수날 증가확인 {sorted_tree}")
    else: # sorted_tree[i] == max_tree:
        i += 1 # 다음 인덱스로 가라
    print(f"현재 위치 i={i-1}, 지금의 날짜는 day{day-1} {sorted_tree} 여기선 물줬어 ")
'''


# 아 문제가 있었네,, 그니깐 이건,, i 를 인덱스가 차기 전까지는 증가시켜주면 안되는거야 맞아맞아



#
# while i < N:
#     # 나는 그니깐 트리를 앞에서부터 물주고 싶은 거고 이 트리에 대해서는 맥스 값이 될 때까지 계속 물을 줄 거임
#     # 이 트리의 크기가 최대치가 아니라면,,
#     if sorted_tree[i] != max_tree:
#         # 이 나무에 대해서는 이제 날짜마다 물을 다르게 주는 걸 생각해줘야 함
#         print(f"i={i} day={day} 트리의 크기 {sorted_tree}")
#         # 홀수번째 날
#         if day % 2 == 1:
#             # 근데 만약 이 홀수날에 맥스와의 차이가 딱 2라서 짝수날에 물을 주고 싶을 수 있잖아
#             if max_tree - sorted_tree[i] == 2:
#                 # 옆 자리에게 물을 줘라
#                 # 근데 일단 옆자리가 있어야겠지?
#                 if i+1 < N:
#                     sorted_tree[i+1] += 1
#                     # 인덱스는 증가시키지 마 아직 증가시킬 때 아냐
#                     # 물줬으면 무조건 데이수는 증가
#                     # 솔직히 여기는 짝수날처럼 고민할 필요가 없어
#                     # 옆자리랑 나무의 크기가 같았어도 걔는 1+1 나는 2 이렇게 증가해서 결국 맞춰지니깐
#                     day += 1
#                     i += 1
#                 # 인덱스 범위를 벗어난다면,, 그냥 하루 기다렸다가 다음날로 보내면 됨
#                 elif i + 1 >= N :
#                     day += 1
#                     # 인덱스는 증가시키지 마
#             else:
#                 sorted_tree[i] += 1
#                 day += 1
#                 i += 1
#         # 짝수번째 날
#         else:
#             if max_tree - sorted_tree[i] == 1:
#                 # 옆 자리에게 물을 줘라
#                 # 근데 일단 옆자리가 있어야겠지?
#                 if i + 1 < N:
#                     # 옆자리에 물을 주고
#                     # 근데 이 옆자리가 나랑 같은 상황이면 안되잖아
#                     if max_tree - sorted_tree[i+1] == 1:
#                         k = 1
#                         while k < N - i:
#                             if sorted_tree[i+k] != max_tree - 1:
#                                 break
#                             k += 1
#                         if k != N - i:
#                             sorted_tree[i + k] += 2
#                             day += 1
#                         elif k == N - 1: # 만약 아주 저 끝까지 갔다면,,
#                             # 나무의 키는 증가시키지 말고 그냥 계속 날짜만 증가시켜주면 될 거 같아
#                             day += 1
#                         # sorted_tree[i + 1] += 2
#                     # 인덱스는 증가시키지 마 아직 증가시킬 때 아냐
#                     # 물줬으면 무조건 데이수는 증가
#                     # 그럼 그냥 옆자리에 물 안주는 경우,, 그냥 시간만 허비해,, 모두가 한 자리만 남았으니깐,,
#                     else:
#                         sorted_tree[i + 1] += 2
#                         day += 1
#                 # 인덱스 범위를 벗어난다면,, 그냥 하루 기다렸다가 다음날로 보내면 됨
#                 elif i + 1 >= N:
#                     # 물 안주는 거야 데이수만 증가하는 거야
#
#                     day += 1
#                     # 인덱스는 증가시키지 마
#             else:
#                 tree[i] += 1
#                 day += 1
#                 i += 1
#             # tree[i] += 2
#             # day += 1
#     else:
#         # 만약 나무의 크기가 맥스와 같다면, 그냥 넘어가주면 된다~ 인덱스만 증가시키면 된다~
#         i += 1
#         # 날짜는 증가시켜 줄 필요 없어 물 안줬으니깐~~~
#         # day += 1
#     print(f"i={i} day={day} 트리의 크기 {sorted_tree}")
# print(day)


하,, 이거 메모이제이션 활용하면 풀 수 있었을거 같은데 ㅜㅜ 시간초과야 ㅜㅜ
dp를 활용하는 걸까?
이거 저번에 한 뭐냐 할튼 그 a형 문제랑 똑같던데,,
내가 DP는 한번도 안해봤구나,,
메모이제이션은 한 결과 저장하고, 그걸 다시 불러오고,, 이러는 거징
