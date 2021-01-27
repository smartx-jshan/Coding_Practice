# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # queue ( each queue has 3 elements)
        queue = collections.deque()
        queue.append([root, -sys.maxsize, sys.maxsize])
        
        while queue:
            # pop from queue
            cur_root, low, high = queue.popleft()
            
            # validate binary tree
            if cur_root.val <= low or cur_root.val >=high:
                return False
            # add queue
            if cur_root.left:
                queue.append([cur_root.left, low, cur_root.val])
            if cur_root.right:
                queue.append([cur_root.right, cur_root.val, high])

        return True
