# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, visited):
            # initializing targetSum inside helper function to access its value
            nonlocal targetSum

            #if node is leaf we return the boolean statement of the comparison between the visitedSum and the targetSum
            if not node.left and not node.right:
                return visited == targetSum

            #we initialize another return variable
            left = False
            # if node has left child we apply recursion and return True or False 
            if node.left:
                left = dfs(node.left, visited + node.left.val)
            #we initialize another return variable
            right = False
            # if node has right child we apply recursion and return True or False
            if node.right:
                right = dfs(node.right, visited + node.right.val)
            # if left is true or right is true, we return true, if both are false, we return false
            return left or right

        # if tree is empty we return false
        if not root:
            return False
        # alternatively we return the result of the DFS
        return dfs(root, root.val)
