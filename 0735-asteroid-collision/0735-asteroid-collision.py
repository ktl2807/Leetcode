class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in asteroids:
            while ans and ans[-1] > 0 > i:
                if ans[-1]< abs(i):
                    ans.pop()
                    continue
                elif ans[-1]==abs(i):
                    ans.pop()
                break
            else:
                ans.append(i)
        return ans
            
