from collections import defaultdict


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # i is the left pointer.
        # count is the time of k repetitions.
        output, i, count, dic = 0, 0, 0, defaultdict(int)
        for j, c in enumerate(s):  # j is the right pointer.
            dic[c] += 1
            if dic[c] == k:
                count += 1  # at least k c's in current window.
            # Contract current window and update left pointer i.

        return output
