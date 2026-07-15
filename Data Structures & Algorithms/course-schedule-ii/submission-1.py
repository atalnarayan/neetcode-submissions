class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+= 1
        
        queue = deque([crs for crs, count in enumerate(indegree) if count == 0])
        out = []

        while queue:
            crs = queue.popleft()
            out.append(crs)
            for child in adj[crs]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return out if len(out) == numCourses else []

            