class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        dic = {i:set() for i in range(n)}
        for k, v in edges:
            dic[k].add(v)
            dic[v].add(k)
            
        leaves = deque([key for key in dic.keys() if len(dic[key]) == 1])
        while n > 2:
            n-=len(leaves)
            count = len(leaves)
            for i in range (count):
                leaf = leaves.popleft()
                neighbor = dic[leaf].pop()
                dic[neighbor].remove(leaf)
                if len(dic[neighbor])==1:
                    leaves.append(neighbor)

        return leaves

                
            
                    
       
                
            


            