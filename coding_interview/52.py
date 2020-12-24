# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        sum = 0
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                if node.val >= low and node.val <= high:
                    sum += node.val
                if node.left:
                    if node.val > low:
                        queue.append(node.left)
                if node.right:
                    if node.val < high:
                        queue.append(node.right)
        
        return sum
