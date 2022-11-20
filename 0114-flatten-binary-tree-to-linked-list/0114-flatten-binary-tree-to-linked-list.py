class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # return root
        if not root:
            return None
        if root.left is not None:
            aux_node = root.right
            root.right = root.left
            root.left = None
            self.attach_aux_node(root.right,aux_node)
            self.flatten(root.right)
        self.flatten(root.right)
        
    def attach_aux_node(self,node,aux_node):
        if node.right is None:
            node.right = aux_node
            return
        self.attach_aux_node(node.right,aux_node)