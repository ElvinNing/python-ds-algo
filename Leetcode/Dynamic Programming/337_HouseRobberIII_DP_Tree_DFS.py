# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        try:
            # Return [a,b], where
            # a = optimal substructure if not robbing node,
            # b = optimal substructure if robbing node.  
            def rob_DP(node):
                if node is None:
                    return [0, 0]
                left = rob_DP(node.left)
                right = rob_DP(node.right)
                # If we don't rob node, we can rob left or not,
                # optimal substructure on the left is max(not rob left, rob left)
                max_no_node = max(left[0], left[1]) + max(right[0], right[1])
                # If we rob node, we are not allow to rob left,
                # optimal substructure on the left has to be not rob left.
                max_with_node = node.val + left[0] + right[0]
                return [max_no_node, max_with_node]
            return max(rob_DP(root))
        except:
            return 0