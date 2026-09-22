# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node.right:
                invert(node.right)
                if node.left:
                    invert(node.left)
                    x = node.right
                    node.right = node.left
                    node.left = x
                else:
                    node.left = node.right
                    node.right = None
            else:
                if node.left:
                    invert(node.left)
                    node.right = node.left
                    node.left = None
                else:
                    return
        if root:
            invert(root)
        return root