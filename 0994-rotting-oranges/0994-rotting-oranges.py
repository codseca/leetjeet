from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for i in range (rows):
            for j in range(cols):
                if (grid[i][j])==2:
                    q.append((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        time=0
        dr=[-1,1,0,0]
        dc=[0,0,-1,1]
        while q:
            l=len(q)
            rotten=False
            for _ in range(l):
                u,v=q.popleft()

                for i in range(4):
                    nr=u+dr[i]
                    nc=v+dc[i]

                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1:
                        q.append((nr,nc)) 
                        grid[nr][nc]=2
                        fresh-=1
                        rotten=  True
            if rotten:
                time+=1

        if fresh>0:
            return -1
        else:
            return time if fresh == 0 else -1


    
                    

