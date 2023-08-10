# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        
        values = self.dfs(root, [])
        ans = float('inf')
        temp = values[-1]
        for i in range(len(values)-2, -1, -1):
            ans = min(ans, temp-values[i])
            temp = values[i]
        return ans

            
        
        
    def dfs(self, root, values):
        if not root:
            return values
        if root.left:
            self.dfs(root.left, values)
        values.append(root.val)
        if root.right:
            self.dfs(root.right, values)
        
       
        
        
        return values