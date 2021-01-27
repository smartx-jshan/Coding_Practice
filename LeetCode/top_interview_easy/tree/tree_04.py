# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # exception
        if root is None:
            return []
        
        # make queue
        queue = collections.deque([root])
        
        # 2x2 array
        result = []
        while queue:
            arr = []
            for _ in range (len(queue)):
                cur_root = queue.popleft()
                arr.append(cur_root.val)
                
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            result.append(arr)
        return result
                
