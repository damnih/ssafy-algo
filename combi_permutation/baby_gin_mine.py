# # 걍 오늘 배운 순열과 조합을 이용해서 만들어 봅시다 하하하하하하
#
# 백트래킹 = 가지치기
#
# 자 나는 nPr 순열을 만들 거야
# 그렇다면 필요한 것은 뭐야?
# 일단, 순열을 만들 n길이의 리스트가 필요하고
# 완성된건 r길이의 리스트겠지
#
# n길이의 리스트를 함수에 넣어줘
# 그러면 여기서 하나를 랜덤하게 뽑아주겠지?
# 걔는 결과 리스트에 넣어줄거얌
# 그 뒤에 나는 얘를 뺀 n-1 길이의 리스트를 다시 함수에 넣어줄거야
# 그러면 여기서 또 하나를 랜덤하게 뽑아주겠지?
# 그 뒤에 나는 또 얘를 뺀 n-2 길이의 리스트를 다시 함수에 넣어줄거야
# ,,,,,,
# 어디까지?
# 결과 리스트가 길이 r이 될 때 까지
# 근데 이건 어케 생각할 수 있다?
# 이 함수를 시행한 횟수를 세보면 됨
# 밖에서 카운트 끌고와서 걔가 r이 되었는지 여부를 확인하면 될 듯 !
#
#
# 근데 나는 6자리에 대해서 전부 다 순열을 만들어줄거니깐
# 솔직히 종료조건은 더 간단하게 생각해줄 수 있음
# 걍 더 선택할 게 없을 때까지 계속 재귀를 돌려줄거임
# 그러니깐 n길이의 리스트가 비엇을때까지만 해주면 되겟네!!!
'''
667767
054600
123456
'''


# remain = list(input())
remain = ['6', '6', '4', '4', '6', '4']
# remain = ['1', '2', '3', '4', '5', '6']
# print(remain)

# is_selected = [False] * len(remain)

def gin_permut(selected, remain):
    # 먼저 종료조건부터 생각
    # remain(=앞으로 고를 예정인, 아직 안고른넘들)이 없을 때까지 해주면 되겠당
    if not remain: # 리메인이 없다면,
        # 함수 끝났으니 뭘 해줄 거야?
        # 만든 순열들 뱉어내야겠징 selected다
        print(selected)
        # return # 새로운넘 호출하는거 끝낸다는 뜻

    # 아니라면, 그냥 계속 만들어줘야 겠지?
    # 근데 나 이거 계속 리스트 접근했자낭..
    # 새로운넘을 뽑아서 팝해주는거는, 항상 맨뒤에서부터하니깐 안되고
    # 그 배열을 전부 다 돌아주면서 해야하는 거잖아?
    # 결국 반복문이다
    else:
        for idx in range(len(remain)):
        # 근데 이거 뽑아주기 전에 생각해야 할 거 있어 먼주알아?
        # 얘를 이미 뽑았던 넘인지 아닌지 판별을 해줘야해
        # 뽑았던 넘인지 아닌지 확인을하는 배열을 만들어주고,
        # 거기서 조회해서 확인해보자 !!! like visited
        # 근데 이 조회하는 배열을 어디서 만들어줘야할까? 함수 밖이다~~~
        # 왜냐하면 함수 내에서 만들어주면, 함수를 호출할 때마다 이게 초기화가 돼 ㅜㅜ
        # 리스트는 글로벌 선언 안해도 조회할 수 있으니깐 좋은거지 야 호
        # 아니네 이거 함수 호출할때마다 초기화해줘야 하기는 해... 가 아닌가  음 아니다 엉 아니야
        # 나 인덱스 접근하는거니깐 ㅇㅇ 맞아맞아 밖이 맞아
        #     if is_selected[idx] == False: # 안뽑았다면
        #         selected_num = remain[idx]
        #         is_selected[idx] = True
        #         selected += [selected_num]
        #
        #         changed_remain = remain[:idx] + remain[idx+1:]
        #         gin_permut(selected, changed_remain)
        #         is_selected[idx] = False
        # 위에까지는 오류 코드
        #     if is_selected[idx]:
        #         continue
        #     is_selected[idx] = True
            selected_num = remain[idx]
            changed_remain = remain[:idx] + remain[idx + 1:]
            # selected = selected + [selected_num]
            gin_permut(selected + [selected_num], changed_remain)
            # is_selected[idx] = False


# 아니 이거 왜 인자로 넣는 selected를 81줄처럼 넣으면 안될까?
# 리스트는 가변이기 때문에 재귀를 계속 호출하면서 변형이 되니깐 문제가 생기는거임
# 아예 변수명을 다르게 만들어서 주던가
# ex)
# selected1 = selected + [selected_num]
# gin_permut(selected1, changed_remain)

# 아니면 저 살아있는 코드처럼 넣을 때 바꿔서 넣어줘야함

# 그리구 궁금한점2
# 왜 여기서는 if is_selected 이거 살려서 하면 하나만 뜰까?
# 결과가 ['6', '5', '4', '3', '2', '1'] 이거 하나 뜨더라,,
# 나는 모든 순열을 찾아주고 싶었던건데,,,
# 여하튼,,
# 그러해,,




gin_permut([], remain)

순열만들어주는 건 다했음