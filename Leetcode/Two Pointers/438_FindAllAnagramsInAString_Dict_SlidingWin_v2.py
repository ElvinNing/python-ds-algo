from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # i is the left pointer.
        # count is the number of characters we need to match.
        output, i, count, dic = [], 0, len(p), defaultdict(int)
        # defaultdict() seems much faster than Counter().
        for c in p:
            dic[c] += 1
        for j, c in enumerate(s):  # j is the right pointer.
            if dic[c] > 0:
                count -= 1
            dic[c] -= 1
            # Contract current window and update left pointer.
            while count == 0:  # Current windows contains all the characters in t.
                # Update possible index.
                if j - i + 1 == len(p):
                    output.append(i)
                # if s[i] is character from t that we count towards 0.
                if dic[s[i]] == 0:
                    count += 1
                dic[s[i]] += 1
                i += 1
        return output
