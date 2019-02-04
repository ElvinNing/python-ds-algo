# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def DFS(node):
            if node:
                if node.left is None and node.right is None:
                    yield node.val
                yield from DFS(node.left)
                yield from DFS(node.right)

        return list(DFS(root1)) == list(DFS(root2))
