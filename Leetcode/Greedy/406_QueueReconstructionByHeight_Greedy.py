class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort people by the first element reversed, then by the second.
        people.sort(key=lambda x:(-x[0], x[1]))  # Python's stable sorting.
        output = []
        for p in people:
            output.insert(p[1], p)
            
        return output