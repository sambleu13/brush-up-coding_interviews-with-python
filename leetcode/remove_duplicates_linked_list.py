# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases, when linked lists is of no elements or 1 element
        if head is None or head.next is None:
            return head
        # use the pointer "current" to traverse linked list
        current = head
        # cycle to repeat as longs as there are element and their next elements
        while current and current.next:
            # as the list is ordered, the duplicate elements will be after the current one
            # if current element equals next element it means the duplicate needs to be removed
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

        
