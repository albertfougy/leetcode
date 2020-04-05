# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# inf / -inf acts as an unbounded upper/lower value for comparison. 
	# This is useful for finding lowest/highest values for something. 
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root: 
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; 
        # contrarily root is the new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceiling)


