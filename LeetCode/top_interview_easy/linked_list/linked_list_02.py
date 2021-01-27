# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # head pointer will be used for return value
        node = head
        
        # find length of LinstNode
        length = 0
        while node:
            length +=1
            node = node.next
        
        # len == 1 case
        if length == 1:
            head = head.next
            return head
        
        # node pointer reset
        node = head
        # deleting node index 
        index = length -n +1
        
        # index pointer
        cur = 0
        # for deleting tail node
        prev_node = None
        while node:
            # find deleting node
            cur +=1
            if cur == index:
                # if current node is tail 
                if not node.next:
                    prev_node.next = None
                    break
                
                node.val = node.next.val
                node.next = node.next.next
                break
            
            prev_node = node
            node = node.next
        
        return head
        
