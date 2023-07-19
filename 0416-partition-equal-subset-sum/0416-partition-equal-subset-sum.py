class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = set([0])
        for num in nums:
            if num > target:
                return False
            elif num == target:
                return True
            new_dp = set()
            for v in dp:
                new_sum = v+num
                if new_sum == target:
                    return True
                elif new_sum < target:
                    new_dp.add(new_sum)
                new_dp.add(v)
            dp = new_dp
        return False

        
    

    