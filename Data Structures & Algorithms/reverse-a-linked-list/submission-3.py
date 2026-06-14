# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # store current element and previos of the current 
        curr, prev = head, None

        while curr:
            curr_temp = curr.next

            curr.next = prev

            prev = curr
            curr = curr_temp

        return prev