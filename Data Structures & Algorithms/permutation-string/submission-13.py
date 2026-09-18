class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for ch in s1:
            s1_count[ord(ch)-ord('a')] += 1
        for ch in s2[:len(s1)]:
            s2_count[ord(ch)-ord('a')] += 1
        l=0
        for r in range(len(s1), len(s2)):
            if s1_count == s2_count: return True
            # grow
            s2_count[ord(s2[r])-ord('a')] += 1
            # shrink
            s2_count[ord(s2[l])-ord('a')] -= 1
            l += 1

        return s1_count == s2_count


