# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath=-float("inf")
        def gainFromsubtree(node):
            nonlocal maxpath
            if not node:
                return 0
            gainFromleft=max(gainFromsubtree(node.left),0)
            gainFromright=max(gainFromsubtree(node.right),0)
            maxpath=max(maxpath,gainFromleft + gainFromright + node.val)
            return max(gainFromleft + node.val,gainFromright + node.val)
        gainFromsubtree(root)
        return maxpath