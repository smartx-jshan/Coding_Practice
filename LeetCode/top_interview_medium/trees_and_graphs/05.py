# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        result = []
        
        def dfs(node: TreeNode): #in-order로 순회를 하면서 순회값을 result 배열에 담는다
            if node.left:
                dfs(node.left)
            
            result.append(node.val)
            
            if node.right:
                dfs(node.right)
            return
        
        node = root
        dfs(node)
        
        if k-1 <= len(result): # result배열에서 k번째 작은 수를 리턴
            return result[k-1]
            
