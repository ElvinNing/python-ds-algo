"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []

        def post(node):
            if not node:
                return []
            for children in node.children:
                post(children)
            output.append(node.val)

        post(root)
        return output
