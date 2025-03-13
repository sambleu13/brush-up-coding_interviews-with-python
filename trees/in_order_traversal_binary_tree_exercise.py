# TODO: Define your Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            

# TODO: Define a binary tree using your Node class
bt_root = Node(1)
bt_root.left = Node(2)
bt_root.right = Node(3)
bt_root.left.left = Node(4)
# TODO: Implement a function to perform in-order traversal

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(str(node.value) + '->', end='')
    in_order_traversal(node.right)
                
# TODO: Print the nodes of the binary tree using the in-order traversal method
in_order_traversal(bt_root)
