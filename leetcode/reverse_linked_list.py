# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize current being the first element, and previous None
        current = head, previous = None
        # while there are elements in the linked list
        while current is not None:
            # the next node saves temporarily the next element in the original linked list
            next_node = current.next
            # the new next current element will be the previous 
            current.next = previous
            # the new previous element will be the current element
            previous = current
            # the new current element will be the temporal next element in the original list
            current = next_node
            # this ensures we traverse the linked list inversely 
        # we return the first element that will be the last element set as previous
        return previous
