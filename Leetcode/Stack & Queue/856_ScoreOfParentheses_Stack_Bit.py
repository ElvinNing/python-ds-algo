class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # layer means the numbers of doubling should apply in the current spot.
        score = layer = 0

        for i, c in enumerate(S):
            if c == '(':
                layer += 1
                # When the iterator meets '()', score is counted.
                if S[i+1] == ')':
                    score += 2**(layer-1)
            elif c == ')':
                layer -= 1

        return score
