# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels_list = []
        queue = collections.deque()

        if root:
            queue.append(root)

        while queue:
            level_len = len(queue)
            curr_level_elems = []
            for i in range(level_len):
                curr_elem = queue.popleft()
                if curr_elem:
                    curr_level_elems.append(curr_elem.val)
                    queue.append(curr_elem.left)
                    queue.append(curr_elem.right)
            if curr_level_elems:
                levels_list.append(curr_level_elems)
            
        return levels_list
