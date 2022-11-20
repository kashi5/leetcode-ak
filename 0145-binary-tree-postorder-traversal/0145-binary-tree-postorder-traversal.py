# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array=[]
        self.pTraversal(root,array)
        return array
    
        
    def pTraversal(self,root,array):
        if root is not None:
            self.pTraversal(root.left,array)
            self.pTraversal(root.right,array)
            array.append(root.val)
        return array
                
                
                
