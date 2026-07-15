class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]


        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([course for course, count in enumerate(indegree) if count == 0])

        count_visited = 0
        while queue:
            count_visited += 1
            curr = queue.popleft()
            for dep in adj[curr]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
        
        return count_visited == numCourses



        