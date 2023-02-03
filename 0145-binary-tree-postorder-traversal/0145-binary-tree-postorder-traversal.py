# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         # array=[]
#         # self.pTraversal(root,array)
#         # return array
#         # 2,3,1
        
#         if root is None:
#             return []
        
#         stack, output = [root, ], []
#         while stack:
#             # root = stack.pop()
#             # if root is not None:
#             #     output.append(root.val)
#             #     if root.right is not None:
#             #         stack.append(root.right)
#             #     if root.left is not None:
#             #         stack.append(root.left)
#             if root.right is not None:
#                 stack.append(root.right)
#             if root.left is not None:
#                 stack.append(root.left)
#             root = stack.pop()
                
        
#         return output
    
        
    # def pTraversal(self,root,array):
    #     if root is not None:
    #         self.pTraversal(root.left,array)
    #         self.pTraversal(root.right,array)
    #         array.append(root.val)
    #     return array
                
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left 
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None
                
        return output
                
                
