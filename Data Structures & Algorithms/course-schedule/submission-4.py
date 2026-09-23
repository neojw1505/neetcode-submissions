class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build adj list
        adj_list = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        path_set = set() # track crs in the current path
        visited_set = set() # tracks crs that cleared all prereqs dont check again

        def dfs(crs): # cycle detector, return True if found cycle, else return False
            # === BASE CASE ===
            if crs in path_set:
                return True

            path_set.add(crs) # add crs to current path

            # === CHECK NEIGHBOURS ===
            for pre in adj_list[crs]: # go through the course prereqs
                if dfs(pre): # detect if that prereq course have a cycle
                    return True # return True that there is a cycle

            path_set.remove(crs) # remove crs from current path
            visited_set.add(crs) # only add if a crs clears all pre-requisites

            return False # return False because no cycle detected
        
        for i in range(numCourses): # numCourses -> 0 to numCourses-1 
            if dfs(i): # dfs each course, check if got cycle
                return False # got cycle -> cannot complete all course -> false
        
        return True # no cycle, can complate all courses -> true
