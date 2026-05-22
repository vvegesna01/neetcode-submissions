class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # init states
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            currState = states[node]
            if currState == VISITED:
                return True
            elif currState == VISITING:
                return False
            
            states[node] = VISITING
            
            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            return True

        for node in preMap:
            if not dfs(node):
                return False
        
        return True
        


            

