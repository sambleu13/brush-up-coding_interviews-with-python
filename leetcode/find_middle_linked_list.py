# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head or head.next:
            # using two pointers, one fast, and one slow
            # as the fast doubles in speed
            # when it reached the end, the slow will reach the middle
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow


