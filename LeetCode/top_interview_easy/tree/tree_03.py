# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # Root = None case
        if root is None:
            return True
        
        # both left and right child are None
        if (not root.left) and (not root.right):
            return True
        
        elif (root.left is None) ^ (root.right is None):
            return False
        
        # transit tree
        queue = collections.deque([root])
        
        cur_root = queue.popleft()
        if cur_root.left:
            queue.append(cur_root.left)
        
        # swap child in left sub-tree
        while queue:
            cur_root = queue.popleft()
            
            # swap child
            cur_root.left, cur_root.right = cur_root.right, cur_root.left
            
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        
        
        # compare left and right trees
        queue_left = collections.deque([root.left])
        queue_right = collections.deque([root.right])
        
        while queue_left:
            cur_root_left = queue_left.popleft()
            cur_root_right = queue_right.popleft()
            
            if cur_root_left.val != cur_root_right.val:
                return False
            
            if (cur_root_left.left is None) ^ (cur_root_right.left is None):
                    return False
            
            if cur_root_left.left:
                queue_left.append(cur_root_left.left)
                queue_right.append(cur_root_right.left)
            
            
            if (cur_root_left.right is None) ^ (cur_root_right.right is None):
                    return False
            
            if cur_root_left.right:
                queue_left.append(cur_root_left.right)
                queue_right.append(cur_root_right.right)
        
        return True
        
