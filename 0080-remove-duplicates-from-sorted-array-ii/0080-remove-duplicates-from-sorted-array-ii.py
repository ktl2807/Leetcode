class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for x in nums:
            if idx < 2 or x != nums[idx-2]:
                nums[idx]=x
                idx+=1
        
        return idx


            

        

