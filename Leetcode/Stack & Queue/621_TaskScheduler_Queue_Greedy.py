from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks)
        m = max(d.values())
        m_count = list(d.values()).count(m)
        return max(len(tasks), (m-1)*(n+1) + m_count)  # need rigorous proof.
