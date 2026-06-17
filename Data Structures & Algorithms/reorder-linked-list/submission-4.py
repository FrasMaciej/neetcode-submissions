# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr_node = head
        while curr_node:
            nodes.append(curr_node)
            curr_node = curr_node.next 
        

        new_head = head
        for i in range(len(nodes) - 1):
            if i % 2 == 0:
                new_head.next = nodes[len(nodes) - 1 - i // 2]
            elif i % 2 == 1:
                new_head.next = nodes[1 + i // 2]

            new_head = new_head.next

        nodes[len(nodes) // 2].next = None