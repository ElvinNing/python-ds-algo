'''Insertion Sort Algorithm

Time Complexity: 
         Comparison   Swap
Worst:    O(n**2)    O(n**2)
Best:     O(n)       O(1)
Average:  O(n**2)    O(n**2)

Space Complexity: O(n), Auxiliary O(1)

Efficient for small data sets (esp. when out-of-order elements are few), adaptive, and stable.

Insertion sort's advantage is that it only scans as many elements as it needs in order to place the k + 1st element, while selection sort must scan all remaining elements to find the k + 1st element.

[1] https://en.wikipedia.org/wiki/Insertion_sort
'''


def insertion_sort(S):
    for i in range(1, len(S)):
        j = i
        while j > 0 and S[j-1] > S[j]:
            S[j], S[j-1] = S[j-1], S[j]
            j -= 1
    return S

if __name__ == "__main__":
    b = [1, 3, 5, 2, 2]
    print(insertion_sort(b))
