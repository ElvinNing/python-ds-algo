'''Quick Selection Algorithm

finding the kth smallest number in an unsorted list or array; such a number is called the kth order statistic.

Time complexity: Worst O(n**2), Expected O(n)

[1] https://en.wikipedia.org/wiki/Selection_algorithm
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
[3] Leetcode Problem 215, https://leetcode.com/problems/kth-largest-element-in-an-array/
'''

import random


def randomized_quick_selection(S, k):
    '''Return the kth smallest element in S'''
    n = len(S)
    if n == 1:
        return S[0]
    p = randomized_hoare_partition(S, 0, len(S)-1)  # pivot index
    if k - 1 == p:
        return S[p]
    elif k - 1 < p:
        return randomized_quick_selection(S[:p], k)
    else:  # k - 1 > idx_p
        return randomized_quick_selection(S[p+1:], k-p-1)


def randomized_hoare_partition(S, l, h):
    p = random.randrange(h)  # Randomly generate the pivot index
    S[p], S[h] = S[h], S[p]
    i, j, pivot = l, h-1, S[h]
    while i <= j:
        while i <= j and S[i] < pivot:
            i += 1
        while i <= j and S[j] > pivot:
            j -= 1
        if i <= j:
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
    S[i], S[h] = S[h], S[i]
    return i


b = [1, 3, 2, 3, 1, 5, 8, 5, 4]
print(randomized_quick_selection(b, 3))
