class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_height_diff(root):
    def height(node):
        # implement this
        if node is None:
            return 0
        else:
            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height, right_height)
        
    if root is None:
        # implement this
        return height(root)
    
    left_height = height(root.left)
    right_height = height(root.right)
    # implement this
    
    height_diff = abs(left_height - right_height)
    max_left = max_height_diff(root.left)
    max_right = max_height_diff(root.right)
    
    max_diff = max(height_diff, max_left, max_right)
    
    return max_diff

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1
