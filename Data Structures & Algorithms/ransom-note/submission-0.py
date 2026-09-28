class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = collections.Counter(magazine)

        for c in ransomNote:
            if c not in magazine_freq:
                return False
            magazine_freq[c] -= 1
            if magazine_freq[c] == 0:
                del magazine_freq[c]
        return True