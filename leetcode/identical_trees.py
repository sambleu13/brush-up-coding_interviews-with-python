# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
    
        def dfs(node, visited = None):
            if visited is None:
                visited = []
            if not node:
                print('null value')
            if node:
                visited.append(node.val)
                if node.left:
                    dfs(node.left, visited)

                if node.right:
                    dfs(node.right, visited)
            

            return visited

        p_lst = dfs(p)
        q_lst = dfs(q)
        print(p_lst, q_lst, p_lst == q_lst)

        if len(p_lst) == len(q_lst):
            if p_lst == q_lst:
                return True
        return False

        
