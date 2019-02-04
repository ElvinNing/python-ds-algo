''' Radix Sort Algorithm

Time Complexity: Worst O(w*n), n keys of word size w
Space Complexity: Worst O(w+N), N is the range of individual digits.

[1] https://en.wikipedia.org/wiki/Radix_sort
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 12.
'''
import itertools


def LSD_radix_sort(S, base=10):
    '''Lease significant digit radix sort of positive integers in S'''
    def bucket_sort_digit(S, base, iteration):
        # Numbers into buckets.
        B = [[] for _ in range(base)]
        for x in S:
            digit = (x // (base ** iteration)) % base
            B[digit].append(x)
        # Buckets to semi-sorted output
        return list(itertools.chain.from_iterable(B))

    it, mx = 0, max(S)
    while base ** it <= mx:
        S = bucket_sort_digit(S, base, it)
        it += 1

    return S


if __name__ == "__main__":
    b = [0, 1, 300, 1010, 1024, 9999, 999, 100, 101, 56, 456]
    print(LSD_radix_sort(b))
