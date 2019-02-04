# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output = temp = ListNode(None)
        temp.next = head
        while temp.next is not None and temp.next.next is not None:
            first = temp.next
            second = temp.next.next
            temp.next = second # temp --> second
            first.next = second.next # first --> third
            second.next = first # second --> first --> third
            temp = first # prepare for the next loop
        
        return output.next
            