class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        bold = [False] * len(s)
        for word in words:  
            start = s.find(word) 
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start+1)
        
        res = []
        n = len(s)
        i = 0
        while i < n:
            # True
            if bold[i]:
                res.append("<b>")
                # add all consequtives bold char
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            # False
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
