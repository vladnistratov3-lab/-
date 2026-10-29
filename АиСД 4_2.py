class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def shiftDown(self, i):
        while i * 2 <= self.size:
            j = self.indMaxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def indMaxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def delMax(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.shiftDown(1)
        return removed

    def getMax(self):
        if self.size == 0:
            return None
        return self.heap[1]


def heap_sort(arr):
    heap = MaxHeap()

    for item in arr:
        heap.insert(item)

    sorted_arr = []
    while heap.size > 0:
        sorted_arr.append(heap.delMax())

    return sorted_arr[::-1]


import sys

data = sys.stdin.read().split()

n = int(data[0])

arr = list(map(int, data[1:1 + n]))

sorted_arr = heap_sort(arr)

print(' '.join(map(str, sorted_arr)))