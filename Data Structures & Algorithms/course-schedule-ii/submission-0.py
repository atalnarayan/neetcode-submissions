class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        state = [0]*numCourses
        stack = list()
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def top_sort(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1
            for child in adj[node]:
                if not top_sort(child):
                    return False

            state[node] = 2
            stack.append(node)
            return True
        
        for crs in range(numCourses):
            if not top_sort(crs):
                return []
        
        return stack