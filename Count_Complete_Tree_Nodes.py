# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def heightleft(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height

        def heightright(node):
            height = 0
            while node:
                node = node.right
                height += 1
            return height
        
        left_height = heightleft(root)
        right_height = heightright(root)

        if left_height == right_height:
            return (1 << right_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        


