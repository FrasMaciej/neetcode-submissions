# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, curr_next = head, None

        while curr:
            # set next for next iteration
            next_node = curr.next
            curr.next = curr_next
            
            # set curr using temporary one for next iteration
            curr_next = curr
            curr = next_node
        
        return curr_next