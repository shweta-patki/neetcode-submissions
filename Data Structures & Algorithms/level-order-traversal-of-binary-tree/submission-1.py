# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        bfs = [root]
        nextLevel = []
        ret = []
        curr = []
        while bfs!=[]:
            node = bfs.pop(0)
            if node.left!=None:
                nextLevel.append(node.left)
            if node.right!=None:
                nextLevel.append(node.right)
            curr.append(node.val)
            if bfs==[]:
                if nextLevel==[]:
                    ret.append(curr)
                    break
                bfs = nextLevel
                nextLevel = []
                ret.append(curr)
                curr = []
        return ret

        