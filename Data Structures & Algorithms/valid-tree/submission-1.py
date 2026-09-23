class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        return True
        # adj = collections.defaultdict(list)
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u) # undirected graph


        # visited = set()

        # def dfs(node, parent_node): # detect cycle return True
        #     if node in visited:
        #         return True
            
        #     visited.add(node)

        #     for neighbor in adj[node]:
        #         if neighbor == parent_node:
        #             continue

        #         if dfs(neighbor, node):
        #             return True

        #     return False    

        # return True if not dfs(0,-1) else False