import sys
import heapq
data = sys.stdin.read().strip().split()
if not data:
    print(0)
n = int(data[0])
if n == 0:
    print(0)
cargoes = []
for i in range(n):
    t = int(data[2 * i + 1])
    l = int(data[2 * i + 2])
    cargoes.append((t, l))
cargoes.sort()
heap = []
max_machines = 0
for arrival, duration in cargoes:
    while heap and heap[0] <= arrival:
        heapq.heappop(heap)
    heapq.heappush(heap, arrival + duration)
    max_machines = max(max_machines, len(heap))
print(max_machines)