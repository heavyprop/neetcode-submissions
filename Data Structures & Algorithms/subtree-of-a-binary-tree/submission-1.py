# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # helper function for detecting the same tree or not
        def isSameTree(p, q):
            # if both empty -> obvs true
            if not p and not q:
                return True
            
            # if vals the same, checkout their children
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            # if none checkout return FALSE
            return False

        # if 2nd tree has no root then always true
        if not subRoot:
            return True
        
        # is 1st tree has no root then it is always false
        if not root:
            return False

        # then if the previous 2 statements don't check out, then we call to check if the same tree
        if isSameTree(root, subRoot):
            return True

        # if none of previous statments check out then check out the different subtrees of the 1st tree, 
        # keep the second the same since it is the smaller tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        