'''Selection Sort Algorithm

Time Complexity: 
         Comparison  Swap
Worst:    O(n**2)    O(n)
Best:     O(n**2)    O(n)
Average:  O(n**2)    O(n)

Space Complexity: O(n), Auxiliary O(1)

Efficient for small data sets and adaptive.
Generally slower than insertion sort.
Not very practical with best case O(n**2)/

In general, insertion sort will write to the array O(n**2) times, whereas selection sort will write only O(n) times. For this reason selection sort may be preferable in cases where writing to memory is significantly more expensive than reading.

[1] https://en.wikipedia.org/wiki/Selection_sort
'''


def selection_sort(S):
    n = len(S)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if S[j] < S[idx_min]:
                idx_min = j
        S[i], S[idx_min] = S[idx_min], S[i]
    return S


b = [1, 3, 5, 4, 4]
print(selection_sort(b))