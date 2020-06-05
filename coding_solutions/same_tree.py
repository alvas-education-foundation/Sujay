"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p,q)]
        while stack :
            x,y = stack.pop()
            if x == None and y ==None:
                continue
            if x == None or y == None:
                return False
            if x.val == y.val:
                stack.append((x.left,y.left))
                stack.append((x.right,y.right))
            else:
                return False
        return True