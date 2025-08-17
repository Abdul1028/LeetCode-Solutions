class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + min(left,right)
