# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check_if_balanced(root)
        return self.is_balanced

    def check_if_balanced(self, root):
        if not root:
            return 0

        left_height = self.check_if_balanced(root.left) 
        right_height = self.check_if_balanced(root.right) 
        if max(left_height, right_height) - min(left_height, right_height) > 1:
            self.is_balanced = False

        return 1 + max(left_height, right_height)