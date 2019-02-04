from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i is the left pointer.
        # count is the time of repetition.
        output, i, count, dic = 0, 0, 0, defaultdict(int)
        for j, c in enumerate(s):  # j is the right pointer.
            if dic[c] > 0:
                count += 1  # c is an repetition.
            dic[c] += 1
            # Contract current window and update left pointer i.
            while count > 0:  # Current window has repetition
                if dic[s[i]] > 1:
                    count -= 1
                dic[s[i]] -= 1
                i += 1
            output = max(output, j - i + 1)
        return output
