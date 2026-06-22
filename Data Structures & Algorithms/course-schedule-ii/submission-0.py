class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]

        # build adjacency list
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        result = []
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            result.append(course)
            state[course] = 2
            return True
    
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result