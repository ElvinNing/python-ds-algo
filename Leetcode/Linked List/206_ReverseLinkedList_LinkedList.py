# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output, input_iter = None, head
        while input_iter is not None:
            # Store the next value in input as the new temp node to iterate.
            temp = input_iter.next
            # Construct the reverse reference 
            # by pointing the next (in input) to previous (in output) 
            input_iter.next = output
            # After the above reference, iterated node is the current output.
            output = input_iter
            # The following means to "remove" current node in the loop.
            input_iter = temp    
        
        return output