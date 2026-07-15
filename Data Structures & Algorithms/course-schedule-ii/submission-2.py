class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+= 1
        
        queue = [crs for crs, count in enumerate(indegree) if count == 0]
        queue_ind = 0

        while queue_ind != len(queue):
            crs = queue[queue_ind]
            for child in adj[crs]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            queue_ind += 1
        
        return queue if queue_ind == numCourses else []

            