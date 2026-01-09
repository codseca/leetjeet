from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
    
        topo = []
        indeg = [0] * numCourses

        # build graph
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)   # b -> a
            indeg[a] += 1        # increase indegree of a

        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            topo.append(node)

            for j in graph[node]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)

        if len(topo) != numCourses:
            return []

        return topo
