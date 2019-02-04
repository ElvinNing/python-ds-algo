'''Quick Sort Algorithm

Time Complexity: Worst O(n**2) rare, Best O(nlogn), Average O(nlogn)

Space Complexity: Auxiliary, Worst O(n), Optimized limit O(logn)

In efficient implementations it is not stable.
Can operate in-place O(logn).
Performs well on large data sets. Slower than insertion sort on small sequence. Outperforms merge-sort and heap-sort on many test.

[1] https://en.wikipedia.org/wiki/Quick_sort
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
'''


def naive_quick_sort(S, l, h):
    if l < h:
        idx_p = naive_partition(S, l, h)
        naive_quick_sort(S, l, idx_p - 1)
        naive_quick_sort(S, idx_p + 1, h)
    return S


def naive_partition(S, l, h):  # Lomuto partition scheme
    i, pivot = l, S[h]
    for j in range(l, h):
        if S[j] < pivot:
            if i != j:
                S[i], S[j] = S[j], S[i]
            i += 1
    S[i], S[h] = S[h], S[i]
    return i


def hoare_partition(S, l, h):
    '''An improved partition scheme by Hoare using two pointers.'''
    # p = random.randrange(h)  # Randomly generate the pivot index
    # S[p], S[h] = S[h], S[p]
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


b = [1, 3, 7, 6, 4, 1, 2, 2, 1, 4]
print(naive_quick_sort(b, 0, len(b)-1))

'''Pivot Selection
Blindly picking the first or last element as pivot leaves it susceptible to the O(n**2) worst case.
1. Randomized Quick Sort
Pick an element of S at random as pivot. Expected O(nlogn).
2. Median-of-3
Choose median of S[l], S[mid], S[h] as pivot.
3. Median of more than 3 elements for large array.
4. Ninther: median of three rule applied with limited recursion.
Med3(S) = median(S[1], S[N/2], S[N])
Ninther(S) = med3(med3(S[1:N/3], med3(S[N/3:2N/3], med3(S[2N/3:N])
'''

'''In-place O(logn) optimization based on tail recursion.

After partitioning, the partition with the fewest elements is (recursively) sorted first, requiring at most O(log n) space. Then the other partition is sorted using tail recursion or iteration, which doesn't add to the call stack.
[1] http://www.cs.nthu.edu.tw/~wkhon/algo08-tutorials/tutorial2b.pdf

About recursion and stack.
[1] https://javascript.info/recursion
[2] https://realpython.com/python-thinking-recursively/
'''


def half_quick_sort(S, l, h):
    '''Quick sort optimized for space usage.'''
    while l < h:
        idx_p = naive_partition(S, l, h)
        if idx_p - l < h - idx_p:
            naive_quick_sort(S, l, idx_p - 1)
            l = idx_p + 1
        else:
            naive_quick_sort(S, idx_p + 1, h)
            h = idx_p - 1
    return S


c = [1, 4, 6, 8, 7, 3, 2, 4, 5]
print(half_quick_sort(c, 0, len(c)-1))
