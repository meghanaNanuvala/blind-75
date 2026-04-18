# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False # first we check subroot exists or not the order of conditions are imp

        if self.sameTree(root, subRoot):
            return True
        
        # if the root subtree is not equal we hv to check whether subroot tree present on left subtree of root or right subtree of root
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))


    def sameTree(self, s, t):
        if not s and not t: return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
        
        return False

