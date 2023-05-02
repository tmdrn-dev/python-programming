from heapq import heappush, heappop, heapify

# heapq는 최소 힙으로 동작한다.
array = [4, 1, 7, 3, 8, 5]
print("Given array: ", array)

minHeap = list()
for i in array:
    heappush(minHeap, i)
print("Min heap(default): ", minHeap)

print("> Pop: ", end='')
while minHeap:
    print(heappop(minHeap), end=' ')
print()

# 최대 힙 구현
maxHeap = list()
for i in array:
    heappush(maxHeap, (-i, i))
print("Max heap: ", maxHeap)

print("> Pop: ", end='')
while maxHeap:
    print(heappop(maxHeap)[1], end=' ')