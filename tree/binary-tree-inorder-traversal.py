# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursively
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)
 
# iteratively       
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right