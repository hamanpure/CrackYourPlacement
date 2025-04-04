# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)  # (depth, lca)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            # If both subtrees have the same depth, current node is LCA
            if left_depth == right_depth:
                return (left_depth + 1, node)
            # If left subtree is deeper, return left LCA
            elif left_depth > right_depth:
                return (left_depth + 1, left_lca)
            # If right subtree is deeper, return right LCA
            else:
                return (right_depth + 1, right_lca)

        return dfs(root)[1]  # Return the LCA node