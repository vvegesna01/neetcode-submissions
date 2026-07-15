class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build adjacency List
        preMap = [[] for i in range(numCourses)]
        print(preMap)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        print(preMap)

        visiting = set()
        visited = set()
        def dfs(node):
            
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False

        return True
