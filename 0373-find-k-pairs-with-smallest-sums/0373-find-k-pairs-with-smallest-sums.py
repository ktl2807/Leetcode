import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        pq=[]
        for i in nums1:
            heappush(pq,(i+nums2[0],i,0))
       
        while k > 0 and pq:
            q, n1, idx = heappop(pq)
            output.append((n1, nums2[idx]))
            if idx+1 < len(nums2):
                heappush(pq,(n1+nums2[idx+1], n1,idx+1))
            k-=1
        return output        

        

            