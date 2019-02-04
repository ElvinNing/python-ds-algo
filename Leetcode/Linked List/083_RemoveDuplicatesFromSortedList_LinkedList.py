# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
            
        output = head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next # Skip head.next since it's duplicate.
            else: 
                head = head.next # Move forward.
            
        return output