class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # create graph of User: [site1, site2, ...]
        visits = sorted(list(zip(timestamp,username,website)))
        G = collections.defaultdict(list)
        for time, user, web in visits:
            G[user].append(web)
        
        # get frequency of 3-sequences
        pattern_count = collections.defaultdict(int)
        for sites in G.values():
            seen = set()
            for i in range(len(sites)-2):
                seq = (sites[i], sites[i+1], sites[i+2])
                seen.add(seq)
            for seq in seen:
                pattern_count[seq] += 1
        
        # get the most common pattern
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
        