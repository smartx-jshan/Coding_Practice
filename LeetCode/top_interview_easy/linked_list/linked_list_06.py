# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # runner method
        slow = fast = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            # if it has cycle, slow and fast are face each other
            if slow == fast:
                return True
        
        # finish loop, fast is not infinite
        return False
