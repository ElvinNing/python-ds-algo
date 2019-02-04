# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = itr = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val
                itr.next = l1 # Refer to l1, the smaller node
                l1 = l1.next # Move forward on l1
            else
                itr.next = l2
                l2 = l2.next # Move forward on l2
            itr = itr.next # Move forward on itr
        itr.next = l1 or l2
        
        return output.next
