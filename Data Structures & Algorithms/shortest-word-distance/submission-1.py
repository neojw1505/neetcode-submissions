class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        shortest = len(wordsDict)

        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                w1 = i
            elif word2 == wordsDict[i]:
                w2 = i
            
            if w1 != -1 and w2 != -1:
                shortest = min(shortest, abs(w1-w2))
        
        return shortest