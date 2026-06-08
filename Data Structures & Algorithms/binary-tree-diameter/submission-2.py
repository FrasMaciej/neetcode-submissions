# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_diameter(root)
        return self.max_depth

    def find_diameter(self, root : Optional[TreeNode]):
        if not root:
            return 0

        height_left = self.find_diameter(root.left)
        height_right = self.find_diameter(root.right)
        curr_node_diameter = height_left + height_right
        self.max_depth = max(self.max_depth, curr_node_diameter)  
        return 1 + max(height_left, height_right)