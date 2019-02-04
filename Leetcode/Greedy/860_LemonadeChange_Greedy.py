class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_5 = count_10 = 0
        for b in bills:
            if b == 5:
                count_5 += 1
            elif b == 10:
                count_10, count_5 = count_10 + 1, count_5 - 1
            elif b == 20:
                if count_10 > 0:
                    count_10, count_5 = count_10 - 1, count_5 - 1
                else:
                    count_5 -= 3
            if count_5 < 0 or count_10 < 0:
                return False
        
        return True
   