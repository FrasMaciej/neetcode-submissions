# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True

        # is_binary_search_tree = True

        # if root.left and root.left.val >= root.val:
        #     is_binary_search_tree = False
        # if root.right and root.right.val <= root.val:
        #     is_binary_search_tree = False

        # is_binary_search_tree = is_binary_search_tree and self.isValidBST(root.left) and self.isValidBST(root.right)

        # return is_binary_search_tree

        def validate(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))