class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Traverse the string and store the last indices of 26 characters in S.
        last_idx = {c: i for i, c in enumerate(S)}
        start = end = 0 # Record the start and end of current substring.
        output = []
        for i, c in enumerate(S):
            end = max(end, last_idx[c]) # Greedy.
            if i == end: # Current string contains all the letters traversed.
                output.append(end - start + 1)
                start = i + 1
                
        return output