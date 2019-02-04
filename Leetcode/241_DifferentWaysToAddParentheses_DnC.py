import operator


class Solution:
    def diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if not s:
            return None
        if s.isdigit():
            return [int(s)]

        output = []
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        # Iterate all possible operators as the last one to be calculated
        # and recur.
        for i, c in enumerate(s):
            if c in '+-*':
                # Divide and conquer
                divide_1 = self.diffWaysToCompute(s[:i])
                divide_2 = self.diffWaysToCompute(s[i+1:])
                for j in divide_1:
                    for k in divide_2:
                        output.append(ops[c](j, k))

        return output
