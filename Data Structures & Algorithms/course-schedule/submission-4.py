class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build an adjacency List
        preMap = {i: [] for i in range(numCourses)}
        print(preMap)
        for crs, pre in prerequisites:
            print(crs)
            preMap[crs].append(pre)
        
        print(preMap)

        visit = set()
        def dfs(course):
            if preMap[course] == []:
                return True
            if course in visit:
                return False

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            
            preMap[course] = []
            visit.remove(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True

        