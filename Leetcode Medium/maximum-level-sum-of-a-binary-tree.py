# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sumAtDepth = defaultdict(int)

        def dfs(node, depth):
            if not node:
                return
            
            sumAtDepth[depth] += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)

        return max(sumAtDepth, key=sumAtDepth.get)
        