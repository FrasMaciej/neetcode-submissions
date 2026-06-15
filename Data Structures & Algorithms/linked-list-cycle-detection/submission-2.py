# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head
        ref_set = set()

        while curr_node:
            if curr_node in ref_set:
                return True
            ref_set.add(curr_node)
            curr_node = curr_node.next

        return False



        