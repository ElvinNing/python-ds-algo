'''Merge Sort Algorithm

Time Complexity: Worst O(nlogn), Best O(nlogn) typical, O(n) variant, Average O(nlogn)

Space Complexity: Auxiliary O(n)

Stable.
More efficient than quicksort for some types of lists if the data to be sorted can only be efficiently accessed sequentially.

[1] https://en.wikipedia.org/wiki/Merge_sort
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
'''


def merge_sort(S):
    n = len(S)
    if n <= 1:
        return S
    m = n // 2
    S1, S2 = S[:m], S[m:]
    merge_sort(S1)  # Recursively sort first half
    merge_sort(S2)  # Recursively sort second half
    merge(S1, S2, S)


def merge(S1, S2, S):
    '''Merge two sorted lists S1 and S2 into S.'''
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


b = [2, 3, 8, 6, 4, 1, 9]
merge_sort(b)
print(b)


# def bottom_up_merge_sort(S):
#     '''Merge sort using bottom-up approach, nonrecursive.'''
