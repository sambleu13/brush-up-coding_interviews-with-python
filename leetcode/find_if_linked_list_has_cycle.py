# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow, fast = head, head
            while fast and fast.next:
                if slow == fast.next:
                    return True
                slow = slow.next
                fast = fast.next.next
        else:
            return False
        
