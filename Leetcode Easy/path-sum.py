class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def has_sum(root,cur_sum):
            if not root:
                return False
            
            cur_sum+=root.val
            
            if not root.left and not root.right:
                return cur_sum==targetSum
            
            return has_sum(root.left,cur_sum) or has_sum(root.right,cur_sum)
        return has_sum(root,0)