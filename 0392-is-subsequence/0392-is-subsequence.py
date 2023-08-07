class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx= 0
        if not s :
            return True
        if not t:
            return False
        for v in t:
            if v == s[idx]:
                idx+=1 
            if idx==len(s):
                return True
        return False
        