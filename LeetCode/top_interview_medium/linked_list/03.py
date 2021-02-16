# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        #싸이클이 없기에 계속 반복해서 돌리다보면 언젠간 같은게 나온다 
        pA = headA
        pB = headB
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            
            if pB:
                pB = pB.next
            else:
                pB = headA
                
            
        return pA
        
        
