# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 1
        maxWidth = 0
        level = 0
        queue = deque([[root, count,1]])
        right = count
        left = count
        while queue:
            node = queue.popleft()
            if node[2]>level:
                maxWidth = max(maxWidth,(right-left+1))
                left = node[1]
                level +=1
                
            right = node[1]
            count = node[1]*2
            if node[0].left:
                queue.append([node[0].left,count, node[2]+1])
            if node[0].right:
                queue.append([node[0].right, count+1, node[2]+1])
        maxWidth = max(maxWidth,(right-left+1))
        return maxWidth
      
