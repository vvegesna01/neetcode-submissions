class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build an adjacency List
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        print(adj_list)

        components = 0
        visited = set()

        def dfs(node):
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components += 1
        
        return components






