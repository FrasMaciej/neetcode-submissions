# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        right_side_visible = []

        while queue:
            curr_level_length = len(queue)
            right_side = None
            for i in range(curr_level_length):
                curr_node = queue.popleft()
                if curr_node:
                    right_side = curr_node
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if right_side:
                right_side_visible.append(right_side.val)

        return right_side_visible