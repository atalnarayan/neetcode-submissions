class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_edges = {i: set() for i in range(numCourses)}
        out_edges = {i: set() for i in range(numCourses)}
        
        for prereq in prerequisites:
            in_edges[prereq[0]].add(prereq[1])
            out_edges[prereq[1]].add(prereq[0])

        queue = deque([])
        for k,v in in_edges.items():
            if len(v) == 0:
                queue.append(k)
        
        index = 0
        while queue:
            course = queue.popleft()
            index += 1
            
            for k in out_edges[course]:
                in_edges[k].remove(course)
                if len(in_edges[k]) == 0:
                    queue.append(k)

        return index == numCourses