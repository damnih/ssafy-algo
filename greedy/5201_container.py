# 편도작성 


# print(burden, truck) # 잘나옴

def container_truck(cargo, truck, N, M):
    # if 하나도 옮길 수 없는 경우 
    # 트럭의 최대 용량이 화물의 최소 용량보다 작음
    if truck[0] < cargo[N-1]:
        return 0
    # 이 경우는 아예 반복을 돌기 전에 딱 한번만 보면 되는거임 
    # 딱 한눈에 보고 되는지 안되는지를 판단하고 싶었던 거잖아 ㅇㅇ 
    # 응 근데 여기도 안돼 아 왜일까~!!!@!@!@@@@~~!!!! 
    # 되네 되네 
    total_cargo = 0
    # 그렇다면 이제 얘를 앞에서부터 순회돌면서 cargo<truck인 애의 cargo들을 더해준다 
    # 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 
    # 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
    for i in range(M): # 트럭 당
        for j in range(N): # 화물의 크기를 비교할거니깐 
            # 이제 평범하게 트럭의 용량에 대해서 화물 내려가며 ㄱㄱㄱ 
            if cargo[j] <= truck[i]:
                total_cargo += cargo[j]
                cargo[j] = 51 # 혹시나 중복해서 고르면 안되니깐 맥스값보다 크게 처리해주장
                # print(total_cargo, cargo)
                # 한번만 담아주면 되니깐 이거 한번 걸린 순간 
                break 
    return total_cargo



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # cargo, truck 
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 일단 짐의 무게와 트럭의 무게를 전부 내림차순 정렬해준당 
    cargo.sort(reverse=True)
    truck.sort(reverse=True)
    # print(cargo, truck)
    ans = container_truck(cargo, truck, N, M)
    print(f'#{tc} {ans}')