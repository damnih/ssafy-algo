import heapq

arr = [20, 15, 19, 4, 13, 11]

# 1. 기본 리스트를 heap으로 만들기
heap_arr = heapq.heapify(arr)
print(arr)

# 힙의 특징은 디버깅이 ㅈㄴ 어렵다는 거임
# [4, 13, 11, 15, 20, 19]
# 라는 결과를 보고 그려봐야 하는거야
# 힙트리를 활용해서 만들어졌기 때문에
# 이거ㅡㅡ


# 2. 하나 씩 데이터를 추가
min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

# 최대 힙

max_heap = []
for num in arr:
    heapq.heappush(max_heap, num)






