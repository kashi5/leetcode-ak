# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        my_dict={}
        result = [False]
        self.bst_helper(root,k,my_dict,result)
        print(my_dict)
        return result[0]
    
    def bst_helper(self,root,k,mydict,out):
        if root and not out[0]:
            self.bst_helper(root.left,k,mydict,out)
            value = k - root.val
            if value in mydict:
                out[0] = True
            mydict.update({root.val:True})
            self.bst_helper(root.right,k,mydict,out)
        return mydict
        