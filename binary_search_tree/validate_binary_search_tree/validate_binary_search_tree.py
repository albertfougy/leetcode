# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # inf / -inf acts as an unbounded ceiling/floor value for comparison.
        # This is useful for finding lowest/highest values for something.
        def helper(node, floor = float('-inf'), ceiling = float('inf')):
            if not node:
                return True

            val = node.val
            if val <= floor or val >= ceiling:
                return False

            if not helper(node.right, val, ceiling):
                return False
            if not helper(node.left, floor, val):
                return False
            return True

        return helper(root)
