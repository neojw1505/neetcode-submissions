class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out_degree = {}
        crs_pre = collections.defaultdict(list)
        pre_crs = collections.defaultdict(list)

        for i in range(numCourses):
            out_degree[i] = 0

        for crs, pre in prerequisites:
            crs_pre[crs].append(pre)
            pre_crs[pre].append(crs)
            out_degree[crs] += 1
        
        queue = collections.deque([])
        for crs, cnt in out_degree.items():
            if cnt == 0:
                queue.append(crs)
        
        res = []
        while queue:
            pre = queue.popleft()
            res.append(pre)
            for crs in pre_crs[pre]:
                out_degree[crs] -= 1
                if out_degree[crs] == 0:
                    queue.append(crs)

        return res if len(res) == numCourses else []