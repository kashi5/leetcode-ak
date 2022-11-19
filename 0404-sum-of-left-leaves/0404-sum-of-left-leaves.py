# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_=[0]
        self.sumLeftLeavesHelper(root,sum_,False)
        return sum_[0]
        
    def sumLeftLeavesHelper(self,root,sum_,isLeftNode):
        if root is None:
            return
        
        left_node = self.sumLeftLeavesHelper(root.left,sum_,True)
        right_node = self.sumLeftLeavesHelper(root.right,sum_,False)
        
        if self.isLeafNode(root) and isLeftNode:
            sum_[0] += root.val
            


    def isLeafNode(self,node):
        if node.left is None and node.right is None:
            return True
        return False