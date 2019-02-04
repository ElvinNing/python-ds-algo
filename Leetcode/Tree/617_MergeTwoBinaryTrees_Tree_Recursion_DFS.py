# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Boolean False
# Any numeric zero: the int value 0, the float value 0.0, the long value 0L, or the complex value 0.0j.	  All other values are considered True.
# Any empty sequence: the str value '', the unicode value u'', the empty list value [], or the empty tuple value ().
# Any empty mapping, such as the empty dict (dictionary) value {}.
# The special value None.

# Let's say you have a class ClassA which contains a method methodA defined as:
# def methodA(self, arg1, arg2):
# do something
# and ObjectA is an instance of this class.
# Now when ObjectA.methodA(arg1, arg2) is called, python internally converts it for you as:
# ClassA.methodA(ObjectA, arg1, arg2)
# The self variable refers to the object itself.


class Solution:
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
            return t
        else:
            return t1 or t2
