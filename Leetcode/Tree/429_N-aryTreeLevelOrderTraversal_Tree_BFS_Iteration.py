"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        try:
            stack, output = [root], []
            while stack:
                values, children_stack = [], []
                for node in stack:
                    values.append(node.val)
                    for c in node.children:
                        children_stack.append(c)
                stack = children_stack
                output.append(values)
            return output
        except:
            return []