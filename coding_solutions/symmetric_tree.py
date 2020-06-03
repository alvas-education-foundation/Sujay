"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val == right.val:
            outside = self.isMirror(left.left, right.right)
            inside = self.isMirror(left.right, right.left)
            return outside and inside

        else:
            return False