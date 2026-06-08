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
                return (0, True)
            
            left_subtree = is_balanced_dfs(root.left)
            right_subtree = is_balanced_dfs(root.right)

            is_height_balanced = left_subtree[1] and right_subtree[1] and abs(left_subtree[0] - right_subtree[0]) <= 1

            return (1 + max(left_subtree[0], right_subtree[0]), is_height_balanced)

        return is_balanced_dfs(root)[1]