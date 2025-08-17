# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def traverse(root):
    #     q = []
    #     val = []
    #     if not root:
    #         return None
        
    #     val.append(root)
    #     if root.left:
    #         q.append(root.left)
        
    #     if root.right:
    #         q.append(root.right)
        
    #     pop = q.pop()


        

        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        result = []
        if root:
            q.append(root)
        
        while q:
            level_size = len(q)
            level_vals = []
            for i in range(level_size):   
                a = q.pop(0)
                level_vals.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            result.append(level_vals)
            
                
        return result



