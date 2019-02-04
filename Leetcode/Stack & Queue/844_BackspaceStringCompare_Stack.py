class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def backward_iter(str):  # A iterator resembles stack
            skip = 0
            for c in reversed(str):
                if c == '#':
                    skip += 1
                elif skip:  # c is not '#' and skip > 0
                    skip -= 1
                else:
                    yield c  # Only yield c when skip <= 0

        return all(x == y for x, y in
                   itertools.zip_longest(backward_iter(S), backward_iter(T)))
