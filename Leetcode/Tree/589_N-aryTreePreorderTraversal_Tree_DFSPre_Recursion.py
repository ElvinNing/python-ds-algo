"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        def pre(node):
            if not node:
                return []
            output.append(node.val)
            for children in node.children:
                pre(children)

        pre(root)
        return output
