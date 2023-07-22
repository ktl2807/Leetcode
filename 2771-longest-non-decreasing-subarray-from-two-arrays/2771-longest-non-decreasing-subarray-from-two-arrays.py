class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cur1 = 1
        cur2 = 1
        maxLen = 1
        l1,l2,l3,l4 = 0,0,0,0
        for i in  range(1, len(nums1)):
           l1 = cur1+1 if nums1[i]>=nums1[i-1] else 1
           l2 = cur1+1 if nums2[i]>=nums1[i-1] else 1
           l3 = cur2+1 if nums1[i]>=nums2[i-1] else 1
           l4 = cur2+1 if nums2[i]>=nums2[i-1] else 1
         
           cur1 = max(l1, l3)
           cur2 = max(l2, l4)

           maxLen = max(cur1, cur2, maxLen)
        return maxLen