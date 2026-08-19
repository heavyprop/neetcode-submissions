# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced is balanced for now
        self.isBalanced = True

        # helper function for checkign depth
        def depth(root):

            # normal b.c.
            if root is None:
                return 0

            # recursively checking the depth
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            # here we are checking the difference between both depths @ each node
            difference = abs(left_depth - right_depth)
        
            if difference > 1:
                self.isBalanced = False

            # normal recursive 
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.isBalanced

        