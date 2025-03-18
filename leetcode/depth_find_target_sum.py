# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, visited = None):
            if visited is None:
                visited = set()
            nonlocal targetSum
            if node:
                visited.add(node.val)
                print(sum(visited))
                if sum(visited) < targetSum:
                    if node.left and node.right:
                        if node.left.val < node.right.val: 
                            dfs(node.left, visited)
                            if sum(visited) >= targetSum:
                                return sum(visited)
                        else:
                            dfs(node.right, visited)
                            if sum(visited) >= targetSum:
                                return sum(visited)
                    if node.left: 
                        dfs(node.left, visited)
                        if sum(visited) >= targetSum:
                            return sum(visited)
                    if node.right:
                        dfs(node.right, visited)
                        if sum(visited) >= targetSum:
                            return sum(visited)

            return sum(visited)
        
        nodes_sum = dfs(root)
        
        if nodes_sum == targetSum and root:
            return True
        return False
