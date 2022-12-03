# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self,rootIdx):
        self.rootIdx = rootIdx
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ti = TreeInfo(0)
        return self.bstHelper(preorder,float("-inf"),float("inf"),ti)
        
    
    def bstHelper(self,arr,low,high,ti):
        if ti.rootIdx == len(arr):
            return None
        
        nodeVal = arr[ti.rootIdx]
        if nodeVal < low or nodeVal > high:
            return None
        
        ti.rootIdx += 1
        lst = self.bstHelper(arr,low,nodeVal,ti)
        rst = self.bstHelper(arr,nodeVal,high,ti)
        return TreeNode(nodeVal,lst,rst)
    
    