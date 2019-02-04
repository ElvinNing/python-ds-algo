from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # i is the left pointer.
        # count is the number of characters we need to match.
        output, i, count, dic = [None, None], 0, len(t), defaultdict(int)
        # defaultdict() seems much faster than Counter().
        for c in t:
            dic[c] += 1
        for j, c in enumerate(s):  # j is the right pointer.
            if dic[c] > 0:
                count -= 1
            dic[c] -= 1  # If c not in t, set count[c] as 0.
            if count == 0:  # Current windows contains all the characters in t.
                # Contract current window.
                while dic[s[i]] < 0:
                    dic[s[i]] += 1
                    i += 1
                # Update possible answer.
                if output == [None, None] or j - i <= output[1] - output[0]:
                    output = [i, j]
                dic[s[i]], i, count = dic[s[i]] + 1, i + 1, count + 1
                
        try:
            return s[output[0]:output[1]+1]
        except:
            return ''
