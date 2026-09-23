class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        crs_pre = collections.defaultdict(list)
        for crs, pre in prerequisites:
            crs_pre[crs].append(pre)
        
        path_set = set()
        visited_set = set()

        def dfs(crs): # True if cycle, else False
            if crs in path_set:
                return True
            if crs in visited_set:
                return False
            
            path_set.add(crs)
            for pre in crs_pre[crs]:
                if dfs(pre):
                    return True
            
            path_set.remove(crs)
            visited_set.add(crs)
            res.append(crs)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
        return res
