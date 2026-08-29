class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # dfs
        visit = set()
        cycle = set()
        topSort = []

        def dfs(crs):
            # got cycle, return false
            if crs in cycle: return False
            # visited before, return true
            if crs in visit: return True

            # add to current path
            cycle.add(crs)
            # check the crs prerequisites
            for pre in preMap[crs]:
                if not dfs(pre): return False # got cycle

            # reach here means no cycle
            visit.add(crs) # pass all prereq
            cycle.remove(crs) # remove crs, backtrack
            topSort.append(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return []
            
        return topSort


