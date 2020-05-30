# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node.right)
                node = node.left
            node = stack.pop()
        return res