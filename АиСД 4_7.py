import heapq
n = int(input())
a = [int(input()) for _ in range(n)]
heap = []
for i in range(n):
    f = a[i]
    wait = max(1000 - f, 1)
    heapq.heappush(heap, (wait, f + 1, i))

time = 0
pos = 0

while heap:
    event_time, new_size, idx = heapq.heappop(heap)
    if event_time < time:
        event_time = time
    travel_time = abs(pos - idx)
    arrival_time = time + travel_time

    if arrival_time <= event_time:
        time = event_time
        pos = idx
        wait = max(1000 - new_size, 1)
        heapq.heappush(heap, (time + wait, new_size + 1, idx))
    else:
        print(event_time)
        break