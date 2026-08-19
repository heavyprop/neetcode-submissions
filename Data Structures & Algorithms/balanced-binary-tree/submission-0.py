# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## do a depth check
        self.isBalanced = True

        # but then also a statement to check if it is balanced
        def depth(root):

            if root is None:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            difference = abs(left_depth - right_depth)
        
            if difference > 1:
                self.isBalanced = False

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.isBalanced

        