class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # condition 1: edges == n-1
        if len(edges) != n-1:
            return False

        # condition 2: no cycle
        visited = set()
        adj = collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visited:
                return True # cycle detected! 

            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node):
                    return True
            return False

        return True if not dfs(0,-1) and len(visited) == n else False 

            

