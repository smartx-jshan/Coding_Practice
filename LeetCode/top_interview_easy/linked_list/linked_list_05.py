# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        
        # make reverse 
        rev = None
        
        while fast and fast.next:
            
            # make reverse
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next
        
        # if the number of elements are odd, slow moves
        if fast:
            slow = slow.next
        
        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True
