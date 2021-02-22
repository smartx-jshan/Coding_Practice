# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        stack = []
        result = []
        if root is None:
            return result
        
        stack.append(root) #노드를 담을 스택
        zig = 0 #지그 재그 플래그
        
        while stack: 
            num = len(stack) #스택의 개수를 미리 확인한 후 스택의 개수만큼 탐색(한 레벨씩 탐색)
            temp = [] # 자식 결과를 담는 어레이
            
            temp_stack = [] #자식을 담는 스택 (큐로하면 이 변순느 삭제 가능)
            for i in range(num):
                node = stack.pop()
                temp.append(node.val)
                
                if zig == 0:
            
                    if node.left:
                        temp_stack.append(node.left)
                    if node.right:
                        temp_stack.append(node.right)
                else:
                    
                    if node.right:
                        temp_stack.append(node.right)
                    if node.left:
                        temp_stack.append(node.left)
            
            stack = stack + temp_stack
            result.append(temp)
            if zig == 0:
                zig = 1
            else:
                zig = 0
        
        return result
        
