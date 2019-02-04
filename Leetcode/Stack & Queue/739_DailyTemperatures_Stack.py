class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        output = [0] * len(T)
        idx = []  # Store indices of T as stack structure
        for i, t in enumerate(T):
            while idx and t > T[idx[-1]]:
                j = idx.pop()
                output[j] = i - j
            idx.append(i)
        
        return output

# For each temperature, push and pop at most once. Time complexity O(2n)