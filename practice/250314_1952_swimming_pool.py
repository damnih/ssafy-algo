import sys
sys.stdin = open("input.txt", "r")

# 완전탐색을 하는 버전
# 각 달에 4가지 케이스를 모두 확인하면서 진행
def recur(month, total_cost):
    # 현재 달을 봐야함, 금액도 봐야함
    if month > 12:
        min_ans = min(min_ans, total_cost)
        return # 카운트 역할을 해주는 거임 사실상 ㅇㅇ

    # 이제 브랜치 부분을 생각해줄거임
    # 1일 이용권으로 다 사는 경우
    recur(month + 1, total_cost + days[month] * cost_day)
    # 1달 이용권 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달 이용권 사는 경우
    recur(month + 3, total_cost + cost_3months)
    # 1년 이용권 사는 경우
    recur(month + 12, total_cost + cost_year)








T = int(input())
for tc in range(1, T+1):
    # 이용권 가격들 # 1일 1달 3달 1년
    cost_day, cost_month, cost_3months, cost_year = map(int, input().split())
    days = [0] + list(map(int, input().split())) # 인덱스 0을 버리기 위한 조치
    min_ans = int(21e8)
    recur(1, 0) # 1월부터 시작하고, 아직 나간 금액은 0원임
    print(f"#{tc} {min_ans}")

# 고작 레벨이 12밖에 안되고 브랜치 경우의 수도 4개씩밖에 없기 떄문에 완탐이어도 시간 걱정 안해도 되더랔ㅋ


