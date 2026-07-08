class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # make a adjacency map:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        print(preMap)
        visiting = set()
        visited = set()
        order = []
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            order.append(course)
            visited.add(course)
            preMap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []


        print(order)
        if len(order) == numCourses:
            return order
        else:
            return []