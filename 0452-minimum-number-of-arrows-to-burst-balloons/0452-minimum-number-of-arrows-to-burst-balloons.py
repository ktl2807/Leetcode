class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key = lambda x : x[1])
        output = 1
        cur_end = points[0][1]
        cur_start = points[0][0]

        for start, end in points[1:]:
            if start > cur_end:
                output+=1
                cur_start = start
                cur_end = end
        
        return output