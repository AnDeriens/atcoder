import heapq

n, m = list(map(int, input().split()))
a = list(map(lambda x: -int(x), input().split()))

heapq.heapify(a)

for i in range(m):
    most_expensive = - heapq.heappop(a)
    most_expensive //= 2
    heapq.heappush(a, - most_expensive)

print(-sum(a))
