from collections import defaultdict


class Solution:
    def LongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i is the left pointer.
        # count is the number of distinct letters.
        output, i, count, dic = 0, 0, 0, defaultdict(int)
        for j, c in enumerate(s):  # j is the right pointer.
            if dic[c] == 0:  # c isn't in dic and default is int() == 0
                count += 1  # c is a new character so count += 1
            dic[c] += 1
            # Contract current window and update left pointer i.
            while count > 2:
                if dic[s[i]] == 1:
                    count -= 1
                dic[s[i]] -= 1
                i += 1
            output = max(output, j - i + 1)
        return output