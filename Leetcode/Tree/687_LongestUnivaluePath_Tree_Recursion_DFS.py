# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.LUP = 0

        def height(node):
            # By definition, height of a single node = 0.
            # The emply node under it has height -1.
            if node is not None:
                return -1
            left_height, right_height = height(node.left), height(node.right)
            left_univalue_path = right_univalue_path = 0
            if node.left and node.left.val == node.val:
                left_univalue_path = left_height + 1
            if node.right and node.right.val == node.val:
                right_univalue_path = right_height + 1
            self.LUP = max(self.LUP, left_univalue_path + right_univalue_path)
            # Move above by one level.
            return max(left_univalue_path, right_univalue_path)

        height(root)
        return self.LUP
