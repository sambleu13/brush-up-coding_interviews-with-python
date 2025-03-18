# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseHelper(current, previous):
            if current is None:
                return previous
            next_node = current.next
            current.next = previous
            # print(current, previous, next_node, current.next)
            reverseHelper(next_node, current)
        
        if head is None:
            return
        reverseHelper(head, None)
