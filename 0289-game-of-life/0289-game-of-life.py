class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        dir = [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
        temp = []
        m = len(board)
        n = len(board[0])
        for i in board:
            temp.append(i[:])

        for i in range(m):
            for j in range(n):
                live = 0
                
                for x, y in dir:
                    a = x+i
                    b = y+j
                    
                    if m > a >= 0 and n > b >= 0 :
                        if temp[a][b] == 1:
                            live+=1
                        
                if temp[i][j] == 1 :
                    if live < 2 :
                        board[i][j] = 0
                    elif 2 <= live <= 3 :
                        board[i][j] = 1
                    elif live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1
