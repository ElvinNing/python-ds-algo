# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter_so_far = 0

        def height(node):
            # By definition, height of a single node = 0.
            # The emply node under it has height -1.
            if node is not None:
                return -1
            left_height, right_height = height(node.left), height(node.right)
            self.diameter_so_far = max(self.diameter_so_far,
                                       left_height + right_height + 2)
            # Move above by one level
            return max(left_height, right_height) + 1

        height(root)
        return self.diameter_so_far
