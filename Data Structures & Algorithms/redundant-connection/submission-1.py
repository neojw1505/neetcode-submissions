class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. build empty adj list, u will draw it out
        adj = collections.defaultdict(list)
        
        # 2. create dfs helper to check if can go from src to dst
        def dfs(src,dst,visited):
            if src == dst:
                return True
            if src in visited:
                return False
            
            visited.add(src)

            for neighbor in adj[src]:
                if neighbor not in visited:
                    if dfs(neighbor, dst, visited):
                        return True
            return False
        
        # 3. build the adj list
        for u,v in edges:
            if dfs(u,v,set()):
                return [u,v]
            
            # draw the line 
            adj[u].append(v) 
            adj[v].append(u)

        
        
