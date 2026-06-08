# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_dfs(root):
            if not root:
                return [True, 0]
            
            left_node = is_balanced_dfs(root.left)
            right_node = is_balanced_dfs(root.right)
            is_balanced = left_node[0] and right_node[0] and abs(left_node[1] - right_node[1]) <= 1

            return [is_balanced, max(left_node[1], right_node[1]) + 1]

        return is_balanced_dfs(root)[0] 