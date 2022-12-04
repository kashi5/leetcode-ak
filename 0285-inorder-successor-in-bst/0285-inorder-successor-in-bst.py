# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack =[]
        current_node = root
        flag = 0
        while current_node is not None or len(stack) !=0:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            node = stack.pop()
            if flag:
                return node
            if node == p:
                flag = 1
            current_node = node.right
        return None
        