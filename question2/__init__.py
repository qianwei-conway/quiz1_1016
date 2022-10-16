class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Question2:
    def areSameTree(self, p, q):

        # if both are null, then true. if either of them is null, then false
        if not p or not q:
            return not p and not q

        return p.val == q.val and self.areSameTree(p.left, q.left) and self.areSameTree(p.right, q.right)

# create two trees
tree1 = [1,2,3,None,4]
tree2 = [1,2,3,4,None]