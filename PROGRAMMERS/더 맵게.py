import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    # scoville 배열을 최소힙에 저장
    for elem in scoville:
        heapq.heappush(heap, elem)
    
    # 힙에서 가장 작은 값이 K보다 작고 heap의 길이가 2보다 같거나 클때(문제의 조건)만 음식을 섞을 수 있음
    while heap[0]<K and len(heap)>=2:
        # 스코빌 지수가 가장 낮은 두 음식을 찾기 위해 pop 두번
        min_one = heapq.heappop(heap)
        min_two = heapq.heappop(heap)
        # 음식을 섞은 뒤
        mix_food = min_one + (min_two * 2)
        # 다시 heap에 푸시
        heapq.heappush(heap, mix_food)
        answer += 1
    
    # 만약 heap의 길이가 2보다 작고 heap의 최소값이 K보다 작으면
    if len(heap)<2 and heap[0]<K:
        # -1을 반환
        return -1

    return answer