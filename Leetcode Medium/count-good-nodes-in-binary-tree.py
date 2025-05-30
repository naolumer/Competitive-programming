class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,max_val):
            if not node:
                return 0
            
            res= 1 if node.val >= max_val else 0

            max_val = max(max_val,node.val)

            res +=dfs(node.left,max_val)
            res +=dfs(node.right,max_val)

            return res
        
        return dfs(root,root.val)