'''Pigeonhole Sort Algorithm

Time Complexity: Worse O(n+N)
Space Complexity: Worse O(n+N)

Specialization of bucket sort. Similar to counting sort.
Performance deteriorates as N grows.

[1] https://en.wikipedia.org/wiki/Pigeonhole_sort
[2] https://en.wikipedia.org/wiki/Pigeonhole_principle
[3] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
'''

import random
import math
import itertools


def pigeonhole_sort(S):
    n, mi = len(S), min(S)
    N = max(S) - mi + 1
    output, B = [None] * n, [0] * N  # B: Bucket
    # Move items to buckets.
    for x in S:
        B[x-mi] += 1
    i = 0
    # Move items out of buckets. O(n+N)
    for j in range(N):
        while B[j] > 0:
            B[j] -= 1
            output[i] = j + mi
            i += 1
    return output


if __name__ == "__main__":
    a = [-1, -3, -1, 1, 3, 5, 2, 2, -2]
    print(pigeonhole_sort(a))


'''Bucket Sort Algorithm

Time Complexity: Worst O(n**2), Best O(n+k), Average O(n+k)
Space Complexity: Worst O(nk)
Distribute the elements of an array into a number of buckets. Each bucket is then sorted individually.

[1] https://en.wikipedia.org/wiki/Bucket_sort
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
[3] http://www.cs.sfu.ca/CourseCentral/307/petra/2009/bucket.pdf
'''


def bucket_sort(S):
    '''Bucket sort, assuming S contains numbers uniformly distributed in [0,1)'''
    n = len(S)
    B = [[] for _ in range(n)]
    # Divide [0,1) into n subintervals as buckets.
    # for each B[i], i/n <= x < (i+1)/n
    for x in S:
        B[int(math.floor(n*x))].append(x)
    for l in B:
        l = insertion_sort(l)
    return list(itertools.chain.from_iterable(B))


def insertion_sort(S):
    for i in range(1, len(S)):
        j = i
        while j > 0 and S[j-1] > S[j]:
            S[j], S[j-1] = S[j-1], S[j]
            j -= 1
    return S


if __name__ == "__main__":
    b = [random.random() for _ in range(10)]
    print(bucket_sort(b))
