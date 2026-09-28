class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = 0
        w2 = 0

        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                w1 = i
            elif word2 == wordsDict[i]:
                w2 = i
        
        return abs(w1-w2)