# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # revert the directions of next pointers in the second half of the linked-list
        prev, curr = None, slow.next
        slow.next = None
        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # change the next pointers to fulfill the task
        first = head
        second = prev

        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_second




