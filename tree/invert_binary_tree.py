"""
Problem: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Category: Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


root = [4,2,7,1,3,6,9]
def inverTree(root):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right) 
    return root


    