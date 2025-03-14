def is_balanced(root) -> bool:
    # returns (height, is_balanced)
    def check_balance(node) -> (int, bool):
        if node is None:
            return 0, True
            
        left_height, left_balanced = check_balance(node.left)
        if not left_balanced:
            return -1, False
        
        right_height, right_balanced = check_balance(node.right)
        if not right_balanced:
            return -1, False

        height = max(left_height, right_height) + 1
        is_balanced = abs(left_height - right_height) <= 1
        return height, is_balanced

    height, balanced = check_balance(root)
    return balanced
