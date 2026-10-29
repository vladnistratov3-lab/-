#include <iostream>
#include <vector>
#include <string>

class MaxHeap {
private:
    std::vector<int> heap;

    void siftUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] >= heap[index]) {
                break;
            }
            std::swap(heap[parent], heap[index]);
            index = parent;
        }
    }

    void siftDown(int index) {
        int size = heap.size();
        while (2 * index + 1 < size) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int largest = left;

            if (right < size && heap[right] > heap[left]) {
                largest = right;
            }

            if (heap[index] >= heap[largest]) {
                break;
            }

            std::swap(heap[index], heap[largest]);
            index = largest;
        }
    }

public:
    void clear() {
        heap.clear();
    }

    void add(int value) {
        heap.push_back(value);
        siftUp(heap.size() - 1);
    }

    bool empty() const {
        return heap.empty();
    }

    int extractMax() {
        if (heap.empty()) {
            return -1;
        }

        int maxValue = heap[0];
        heap[0] = heap.back();
        heap.pop_back();

        if (!heap.empty()) {
            siftDown(0);
        }

        return maxValue;
    }
};

int main() {
    MaxHeap heap;
    std::string command;

    while (std::cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        }
        else if (command == "ADD") {
            int n;
            std::cin >> n;
            heap.add(n);
        }
        else if (command == "EXTRACT") {
            if (heap.empty()) {
                std::cout << "CANNOT" << std::endl;
            }
            else {
                int maxValue = heap.extractMax();
                std::cout << maxValue << std::endl;
            }
        }
    }

    return 0;
}