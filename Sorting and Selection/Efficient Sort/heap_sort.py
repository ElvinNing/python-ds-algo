''' Heap Sort Algorithm

Time Complexity: Worst O(n*logn), Best O(nlogn) or O(n), Average O(nlogn)

Space Complexity: Auxiliary O(1)


[1] https://en.wikipedia.org/wiki/Heapsort
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 9.
'''

import heapq


def heap_sort(S):
    heapq.heapify(S)  # Construct a heap from S, O(n) in-place.
    return [heapq.heappop(S) for _ in range(len(S))]  # return the smallest


b = [2, 3, 7, 1, 4, 1, 8]
print(heap_sort(b))
