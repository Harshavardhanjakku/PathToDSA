import heapq

heap = []
heapq.heappush(heap, 101)
heapq.heappush(heap, 4)
heapq.heappush(heap, 30)
heapq.heappush(heap, 70)

print("Heap:", heap)              # Heap: [3, 4, 11, 7]
print("Popped:", heapq.heappop(heap))  # Popped: 3
print("Popped:", heapq.heappop(heap))  # Popped: 4
print("Popped:", heapq.heappop(heap))  # Popped: 7
