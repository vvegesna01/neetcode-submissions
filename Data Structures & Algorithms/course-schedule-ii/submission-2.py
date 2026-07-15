class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        visiting = set()
        output = []
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            output.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output
