# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as dq
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if root is empty, solution is depth 0
        if not root:
          return 0
        # initialize double ended queue with dq 
        queue = dq()
        # append the root node of the tree and its depth as tuple
        queue.append((root, 1))
        # whhile there are nodes in the tree
        # search for the leaft (node without right or left children)
        while queue:
          # initialize the current node and depth by poping left from queue
          # unpacking values
          vertex, depth = queue.popleft()
          # if vertex is leave return depth
          if not vertex.right and not vertex.left:
            return depth
          # if not continue appending to queue and search if next nodes are leaves
          if vertex.left:
            queue.append((vertex.left, depth + 1))
          if vertex.right:
            queue.append((vertex.right, depth + 1))
