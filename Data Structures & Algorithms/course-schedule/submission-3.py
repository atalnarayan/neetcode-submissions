class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        state = [0]*numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        def has_cycle(crs):
            if state[crs] == 1:
                return True
            
            if state[crs] == 2:
                return False
            
            state[crs] = 1
            for child in adj[crs]:
                if has_cycle(child):
                    return True

            state[crs] = 2
            return False

        for crs in range(numCourses):
            if has_cycle(crs):
                return False
        
        return True

        