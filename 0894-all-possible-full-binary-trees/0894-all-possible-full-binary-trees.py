# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0:
            return []
        
        trees = []
        if n == 1:
            return [TreeNode(0)]
        
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-i-1)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    trees.append(root)
        
        return trees

    

            