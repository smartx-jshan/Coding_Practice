# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        
        if not head or (head and not head.next): #헤드와 그 뒤에 헤드가 없으면
            return head
        
        odd_tail = head
        even_tail = head.next
        
        while even_tail.next: #even_tail의 다음 요소가 있으면
            
            node = even_tail.next 
            temp = odd_tail.next
            odd_tail.next = node
            even_tail.next = node.next
            node.next = temp
            odd_tail = odd_tail.next
            
            if even_tail.next: 
                even_tail = even_tail.next
            else: #even_tail의 next가 없을 수도 있다.
                break #그럼 종료
        
        return head
        
        
        
        
