class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # for each node ...
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
            
        return count 
