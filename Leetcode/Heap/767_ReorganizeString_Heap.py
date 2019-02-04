# A heap is a natural structure to repeatedly return the current top 2 letters 
# with the largest remaining counts.
# https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = Counter(S)
        # Not possible to output since the most common letter is too many.
        if count.most_common(1)[0][1] > (len(S) + 1)/2:  # O(nlogk) = O(n)
            return ''
        h = [(-count[c], c) for c in count.keys()]  # Use -count for minheap
        heapq.heapify(h)
        output = []
        while len(h) >= 2:
            k1, c1 = heapq.heappop(h)
            k2, c2 = heapq.heappop(h) 
            output.extend([c1, c2])  # c!= output[-1] is unnecessary
            if k1 <= -2:  # if c1 is not depleted.
                heapq.heappush(h, (k1 + 1, c1))
            if k2 <= -2:
                heapq.heappush(h, (k2 + 1, c2))
        if h:  # len(S) is odd, h is not empty
            output.append(h[0][1])
 
        return ''.join(output)

# heapq.most_common(k):
# List the k most common elements and their counts from the most
# common to the least, using heapq.nlargest(k).
# If k is None, then list all element counts using sorted().
