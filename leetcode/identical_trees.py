# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are empty
        if not p and not q:
            return True
        # if one is empty or their values are different
        if not p or not q or p.val != q.val:
            return False
        # iterate recursively their left and right childes and if both are true or false, return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
