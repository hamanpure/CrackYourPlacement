# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recover(root, 0)
    def recover(self, root, val):
        if root is None:
            return 
        root.val = val
        self.values.add(val)

        self.recover(root.left, val*2+1)
        self.recover(root.right, val*2+2)

    def find(self, target: int) -> bool:
        return target in self.values        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)