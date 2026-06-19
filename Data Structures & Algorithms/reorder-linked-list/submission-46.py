# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Split linked list to two halves
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Re-order second half of the linked list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # change the links to fulfill the task
        left, right = head, prev
        while right:
            tmp_left_next, tmp_right_next = left.next, right.next
            left.next = right
            right.next = tmp_left_next
            left, right = tmp_left_next, tmp_right_next



