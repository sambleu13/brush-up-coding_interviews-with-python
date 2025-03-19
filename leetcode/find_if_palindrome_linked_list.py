# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        
        for _ in range(len(stack)):
            stack_element = stack.pop()
            #print(head.val, stack_element)
            if stack_element != head.val:
                return False
            head = head.next
        return True
            
            
