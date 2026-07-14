class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            adj[prereq[1]].append(prereq[0])

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            
            for k in adj[course]:
                indegree[k] -= 1
                if indegree[k] == 0:
                    queue.append(k)
                
        return count == numCourses