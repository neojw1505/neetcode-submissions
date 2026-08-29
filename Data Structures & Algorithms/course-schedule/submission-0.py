class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. create adj list
        preMap =  { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # dfs 
        visited = set()
        def dfs(crs):
            # got cycle = False
            if crs in visited:
                return False
            # no prerequisite = True
            if preMap[crs] == []:
                return True
            
            # if not visiting this course, so add to visited
            visited.add(crs)
            # dfs the prerequisites of the current crs
            for pre in preMap[crs]:
                # if any prerequisite return False, all False
                if not dfs(pre): return False
            
            visited.remove(crs) # remove the curr crs so that it can be use in other path
            preMap[crs] = [] # next path don't need recalculate
            return True # all prequisite can, return True

        # this is to ensure all course gets checked, cause the graph might be disconnected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


