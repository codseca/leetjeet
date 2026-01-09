class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        vis=[0]*n
        c=0
        def dfs(city):
            
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not vis[neighbour]:
                    vis[neighbour]=1
                    dfs(neighbour)

        for city in range(n):
            if not vis[city]:
                c += 1
                vis[city] = True
                dfs(city)
        return c

 