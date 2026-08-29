from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram means reaarange words can form same word
        # if not same length return false
        if len(s) != len(t):
            return False
        
        # freq of each letter
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count
