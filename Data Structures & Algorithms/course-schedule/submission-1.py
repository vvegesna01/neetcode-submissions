class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        # build graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # build states array
        # 0 = unvisited
        # 1 = processing
        # 2 = processed
        state = [0] * numCourses
        print("state:", state)

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2
            return True
                

        for course in range(numCourses):
            print("currentCourse", course)
            if not dfs(course):
                return False
            
        
        return True
