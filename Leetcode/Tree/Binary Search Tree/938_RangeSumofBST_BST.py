# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        self.output = 0
        def dfs_pre(node):
            if node:
                if L <= node.val <= R:
                    self.output += node.val
                if node.val > L:
                    dfs_pre(node.left)
                if node.val < R:
                    dfs_pre(node.right)
        dfs_pre(root)
        return self.output
