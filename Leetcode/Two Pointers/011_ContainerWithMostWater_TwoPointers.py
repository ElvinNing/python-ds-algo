class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        A = min(height[i], height[j]) * (j-i)
        
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            h = min(height[i], height[j])
            A = max(A, h * (j-i))
        
        return A
