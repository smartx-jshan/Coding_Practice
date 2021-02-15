# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0) # 노드 저장
        node = head #헤드의 이동 포인터
        
        carry = 0
        while l1 or l2 or carry: 
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            sum = sum + carry #캐리가 이전에 있다면 sum에 합쳐준다
            
            carry, val = divmod(sum, 10)
            node.next = ListNode(val)
            node = node.next
        return head.next
