class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # setup
        s1_dict = collections.Counter(s1)
        s2_dict = collections.defaultdict(int)
        len_s1 = len(s1)
        len_s2 = len(s2)
        for i in range(len_s1):
            s2_dict[s2[i]] += 1
        
        l=0 
        r=len_s1-1
        while r < len_s2:
            if s1_dict == s2_dict:
                return True
            if r+1 >= len_s2:
                break
            # grow map 
            r += 1
            s2_dict[s2[r]] += 1
            # shrink map
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
            l += 1


        return False
        
# s1="ab" {a:1,b:1}
# s2="lecabee" {b:1,e:1}
        
