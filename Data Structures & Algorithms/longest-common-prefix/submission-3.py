class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = []
        while True:
            if i >= len(strs[0]):
                return "".join(ans)
            currnet_char = strs[0][i]

            for s in strs:
                if i < len(s) and currnet_char == s[i]:
                    continue
                else:
                    return "".join(ans)
            ans.append(currnet_char)
            i += 1 

