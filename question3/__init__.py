class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Question3:
    def levelOrderTraversal(self, root):

        res = []
        queue = [root]

        if not root:
            return res

        while queue:
            node = queue.pop(0)

            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res