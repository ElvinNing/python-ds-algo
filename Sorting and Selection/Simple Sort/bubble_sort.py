'''Optimized Bubble Sort Algorithm

Time Complexity: Worst O(n**2), Best O(n), Average O(n**2)
Space Complexity: Auxiliary O(1)
The only significant advantage is adaptive, namely to detect that the list is sorted efficiently is built into the algorithm.
It runs slower than insertion sort and is not a practical sorting algorithm.    

[1] https://en.wikipedia.org/wiki/Bubble_sort
'''


def optimized_bubble_sort(S):
    n = len(S)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if S[i-1] > S[i]:
                S[i-1], S[i] = S[i], S[i-1]
                new_n = i
        n = new_n
    return S


b = [1, 3, 5, 6, 5]
print(optimized_bubble_sort(b))
