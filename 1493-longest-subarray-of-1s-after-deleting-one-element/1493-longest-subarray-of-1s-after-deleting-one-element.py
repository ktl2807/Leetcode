class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        cur = 0
        maxSize = 0
        for num in nums:
            if num ==1:
                cur+=1
                maxSize = max(maxSize, pre+cur)
            else:
                pre = cur
                cur = 0
        if maxSize == len(nums):
            maxSize -=1
        return maxSize
        