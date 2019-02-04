'''Counting Sort Algorithm

Sorting a collection of n objects according to keys that are SMALL INTEGERS in the range [0, N-1].

Time Complexity: Average O(n+N)
Space Complexity: Worst O(n+N)

[1] https://en.wikipedia.org/wiki/Counting_sort
'''


def counting_sort(S):
    '''Simplified counting sort assuming S is collection of integer keys.'''
    n, N = len(S), max(S) + 1
    output, count = [None] * n, [0] * N
    for x in S:
        count[x] += 1
    # Modify count as starting indices of keys.
    # count[k] = start index of k in output.
    total = 0  # total number of elements before current iteration
    for i in range(N):
        temp = count[i]
        count[i] = total
        total += temp
    # Copy to output array.
    for x in S:
        output[count[x]] = x
        count[x] += 1
    
    return output

b = [1, 3, 5, 6, 5]
print(counting_sort(b))