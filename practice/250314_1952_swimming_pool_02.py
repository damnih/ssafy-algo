

T = int(input())
for tc in range(1, T+1):

    dp[2] = dp[1] + min(days[2] * cost_day, cost_month)


    # 3월~12월은 반복하면서 계산
    for month in range(3, 13):
        # 3월의 최소 비용 후보
        # 1. 1월에 3개월 이용권을 구입한 경우
        # 2. 2월의 최소비용 + 1일권 구매
        # 3. 2월의 최소비용 + 1달권 구매
        dp[month] = min(dp[month-3] + cost_3months
                        , dp[month-1] + (days[month] + cost_day)
                        , dp[month-1] + cost_month)

    # 값이 고정되면 이런 식으로 그냥 계속 조회해서 긁어오는 식으로 할 수 잇음



완탐이나 재귀호출 중심으로 문제를 먼저 풀고, 이게 익숙해졌다 싶으면 디피문제 기초만 좀 풀길,,

완탐 재귀 ㅇㅇ

요 유형들은 반드시 익혀주셔야 합니다 ㅜ
