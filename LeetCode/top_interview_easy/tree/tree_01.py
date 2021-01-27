# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # exception
        if root is None:
            return 0
        
        # queue 
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth +=1
            # repeat the current number of elements in queue
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            
        return depth 
        
