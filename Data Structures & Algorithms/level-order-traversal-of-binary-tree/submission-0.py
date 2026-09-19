# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        lis = []
        def traverse(node, level):
            if node == None:
                return
            if level in dic:
                dic[level].append(node.val)
            else:
                dic[level] = [node.val]
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        traverse(root, 0)
        for i in range(len(dic)):
            lis.append(dic[i])
        return lis
