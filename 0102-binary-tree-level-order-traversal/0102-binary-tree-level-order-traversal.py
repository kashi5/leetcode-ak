# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        level = 0
        if not root:
            return levels
        self.helperLevelOrder(root,level,levels)
        return levels
    
    def helperLevelOrder(self,root,level,levels):
        if len(levels) == level:
            levels.append([])
        levels[level].append(root.val)
        if root.left:
            self.helperLevelOrder(root.left,level+1,levels)
        if root.right:
            self.helperLevelOrder(root.right,level+1,levels)
        