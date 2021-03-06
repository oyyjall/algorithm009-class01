# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node:
                if color == white:
                    stack.append((white, node.right))
                    stack.append((gray, node))
                    stack.append((white, node.left))
                else:
                    res.append(node.val)
        return res