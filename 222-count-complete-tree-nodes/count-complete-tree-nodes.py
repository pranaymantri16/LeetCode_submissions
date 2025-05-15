class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(node, goLeft=True):
            height = 0
            while node:
                height += 1
                node = node.left if goLeft else node.right
            return height
        if not root:
            return 0
        left_height = getHeight(root, True)
        right_height = getHeight(root, False)
        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
