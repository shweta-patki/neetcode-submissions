# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        bfs = deque()
        bfs.append(root)
        nextL = deque()
        ret = []
        curr = []
        while bfs:
            node = bfs.popleft()
            curr.append(node.val)
            if node.left:
                nextL.append(node.left)
            if node.right:
                nextL.append(node.right)
            if bfs==deque() and nextL:
                bfs = nextL
                nextL = deque()
                ret.append(curr)
                curr = []
        ret.append(curr)
        return ret