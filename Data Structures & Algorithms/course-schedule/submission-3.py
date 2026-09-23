class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build adj list
        adj_list = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        state = {} 
        path_set = set()
        def dfs(crs): # cycle detector, return True if found cycle, else return False
            # === BASE CASE ===
            if crs in path_set:
                return True

            path_set.add(crs)
            # === CHECK NEIGHBOURS ===
            for pre in adj_list[crs]: # go through the course prereqs
                if dfs(pre): # detect if that prereq course have a cycle
                    return True # return True that there is a cycle
            path_set.remove(crs)
            
            return False # return False because no cycle detected
        
        for i in range(numCourses): # numCourses -> 0 to numCourses-1 
            if dfs(i): # dfs each course, check if got cycle
                return False # got cycle -> cannot complete all course -> false
        
        return True # no cycle, can complate all courses -> true
