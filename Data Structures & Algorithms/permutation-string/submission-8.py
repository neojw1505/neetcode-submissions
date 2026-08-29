class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # build unique key for s1
        key_1 = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord('a')
            key_1[idx] += 1
        
        # use sliding window of len(s1) and iterate through s2 and try to find a match with 
        # the unique key_1, if match return True, else at the end return False
        for i in range(len(s2) - len(s1) + 1):
            key_2 = [0] * 26
            for ch in s2[i:i+len(s1)]:
                idx = ord(ch) - ord('a')
                key_2[idx] += 1
            if key_1 == key_2: return True
        
        return False
                
