class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
    
        visiting = set()
        visited = set()
        res = []
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res