# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            count = 0
            node = head
            middle_list = []
            while node:
                print(node.val, node.next)
                node = node.next
                count += 1
            i = 0
            count = int(count / 2)
            print(count)
            current = head
            while i < count:
                current = current.next
                i += 1
            return current
        else:
            return None

