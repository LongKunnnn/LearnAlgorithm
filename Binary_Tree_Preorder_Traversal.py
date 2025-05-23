# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def check(node):
            if not node:
                return 
            result.append(node.val)
            check(node.left)
            check(node.right)

        check(root)
        return result


            

        