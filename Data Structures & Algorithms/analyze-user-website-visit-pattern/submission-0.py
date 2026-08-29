class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1. sort visit based off timestamp 
        visits = list(zip(timestamp, username, website))
        visits.sort() # sort in-place

        # 2. create adj list, User:[site1, site2, site3]
        user_sites = collections.defaultdict(list)
        for time,user,web in visits:
            user_sites[user].append(web)
        
        # 3. count most frequent pattern
        pattern_count = collections.defaultdict(int)
        for sites in user_sites.values():
            seen = set()
            for i in range(len(sites)-2): # 3 sites at a time
                seq = (sites[i], sites[i+1], sites[i+2])
                seen.add(seq)
            for seq in seen:
                pattern_count[seq] += 1
        
        # 4. return most frequent pattern
        max_cnt = 0
        max_pattern = ""
        for pattern, cnt in pattern_count.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_pattern = pattern
            elif cnt == max_cnt:
                if pattern < max_pattern:
                    max_pattern = pattern
        return list(max_pattern)
            



