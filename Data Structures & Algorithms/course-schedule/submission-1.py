class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build adj list
        adj_list = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        state = {} 

        def dfs(crs): # cycle detector, return True if found cycle, else return False
            if state.get(crs) == "VISITING": # trip on itself
                return True
            if state.get(crs) == "VISITED": # crs already cleared
                return False 
            
            # not VISITING or VISITED means current course is UNVISITED
            # change it to visting
            state[crs] = "VISITING"

            for pre in adj_list[crs]: # go through the course prereqs
                if dfs(pre): # detect if that prereq course have a cycle
                    return True # return True that there is a cycle
            
            # since all prereqs are cleared
            state[crs] = "VISITED"
            return False # return False because no cycle detected
        
        for i in range(numCourses): # numCourses -> 0 to numCourses-1 
            if dfs(i): # dfs each course, check if got cycle
                return False # got cycle -> cannot complete all course -> false
        
        return True # no cycle, can complate all courses -> true
            
            



