class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self._recover(root, 0)

    def _recover(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val
        self.values.add(val)
        if node.left:
            self._recover(node.left, 2 * val + 1)
        if node.right:
            self._recover(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values
