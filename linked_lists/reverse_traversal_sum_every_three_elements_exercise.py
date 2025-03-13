class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_sum(head):
    stack = []
    while head:
        # implement this
        stack.append(head.data)
        head = head.next

    sum_, index = 0, 1
    while stack:
        # implement this
        if index % 3 == 0:
            sum_ += stack.pop()
        stack.pop()
        index += 1
    
    return sum_
    
