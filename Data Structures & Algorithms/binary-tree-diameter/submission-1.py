# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.nodes_diameter(root)
        return self.max_depth


    def nodes_diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.nodes_diameter(root.left)
        r = self.nodes_diameter(root.right)
        curr_diameter = l + r
        self.max_depth = max(self.max_depth, curr_diameter)
        return 1 + max(l, r)