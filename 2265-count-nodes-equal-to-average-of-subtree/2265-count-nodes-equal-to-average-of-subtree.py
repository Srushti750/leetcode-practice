# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_dfs(self, node):
        if node is None:
            return 0,0
        
        left_sum, left_count = self.tree_dfs(node.left)
        right_sum, right_count = self.tree_dfs(node.right)

        total = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1

        average = total // total_count

        if average == node.val:
            self.result += 1

        return total, total_count

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0
        self.tree_dfs(root)
        return self.result

        