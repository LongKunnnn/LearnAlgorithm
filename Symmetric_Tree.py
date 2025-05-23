
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @staticmethod  
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        def isMirror(t1 : Optional[TreeNode], t2 : Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            return(
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )

        if not root:
            return True
        return isMirror(root.left, root.right)
        