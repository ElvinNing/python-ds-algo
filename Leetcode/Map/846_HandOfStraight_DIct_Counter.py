from collections import Counter


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        N = len(hand)
        if N % W != 0:
            return False
        count = Counter(hand)
        while count:  # count isn't empty.
            mi = min(count)  # Minimum among keys.
            for k in range(mi, mi + W):
                if k not in count:  # k isn't in hand or count.
                    return False
                if count[k] == 1:
                    del count[k]
                else:
                    count[k] -= 1
        return True
