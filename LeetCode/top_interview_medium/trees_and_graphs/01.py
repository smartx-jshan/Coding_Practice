# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def dfs(node): #탐색을 한다 
            
            if node is None: #노드가 없으면 나가기
                return
            
            dfs(node.left) #왼쪽부터 쭉
            result.append(node.val) 
            dfs(node.right) #그리고 오른쪽
        
        dfs (root)
        
        return result
