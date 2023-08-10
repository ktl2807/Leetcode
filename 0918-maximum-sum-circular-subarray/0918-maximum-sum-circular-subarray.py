class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return nums[0]
        maxTotal = nums[0]
        maxSum = nums[0]
        minSum = nums[0]
        minTotal = nums[0]
        for i in nums[1:]:
            maxSum = max(maxSum+i, i)
            maxTotal = max(maxSum, maxTotal)
            minSum = min(minSum+i, i)
            minTotal = min(minSum, minTotal)
            
        output = max(maxTotal, sum(nums)-minTotal)
        if output != 0:
            return output
        else:
            return maxTotal