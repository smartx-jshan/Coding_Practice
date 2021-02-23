"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None: #예외 처리
            return root 
        
        queue = collections.deque([root]) #먼저 루트를 큐에 집어넣고
        
        while queue:
            pop = queue.popleft() #하나를 뺀다
            
            size = len(queue) #하나 빼고 난뒤 사이즈를 알아낸뒤
            
            if pop.left: #자식이 있으면 큐에 넣는다
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)
                
            
            for i in range(size): #하나 뺀 큐 사이즈만큼 반복
                pop.next = queue.popleft()
                pop = pop.next
                
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                    
            #기본적으로 next = None으로 되어있으므로 None에 대한 처리는 생략
        return root
            
            
        
        
