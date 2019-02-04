class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use dictionary to achieve O(1) for c in dic.
        # i is the left pointer.
        # dic = {(k -> v): character -> index in s}
        output, i, dic = 0, 0, {}
        for j, c in enumerate(s):  # j is the right pointer.
            if c in dic and dic[c] >= i: 
                i = dic[c] + 1
            dic[c] = j
            output = max(output, j - i + 1)
        return output
