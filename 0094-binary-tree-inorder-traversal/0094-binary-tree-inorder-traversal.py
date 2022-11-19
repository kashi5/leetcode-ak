# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # array=[]
        # return inorderHelper(root,array)
        return inOrderIterative(root)
    
# def inorderHelper(root,array):
#     if root is not None:
#         inorderHelper(root.left,array)
#         array.append(root.val)
#         inorderHelper(root.right,array)
#     return array
      
def inOrderIterative(root):
    res,stack=[],[]
    curr = root
    while curr is not None or len(stack)!=0 :
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res