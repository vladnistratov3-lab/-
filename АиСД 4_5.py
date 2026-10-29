import heapq


n = int(input())
numbers = list(map(int, input().split()))

heapq.heapify(numbers)
total_cost = 0.0

while len(numbers) > 1:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    s = a + b
    cost = s * 0.05
    total_cost += cost
    heapq.heappush(numbers, s)

print(f"{total_cost:.2f}")