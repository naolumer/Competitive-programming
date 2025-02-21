# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # ITERATIVE SOLUTION
        
        # cur = root

        # while cur and cur.val!=val:
        #     if val<cur.val:
        #         cur = cur.left
        #     else:
        #         cur = cur.right
        # return cur

        # RECURSIVE SOLUTION

        if not root:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)