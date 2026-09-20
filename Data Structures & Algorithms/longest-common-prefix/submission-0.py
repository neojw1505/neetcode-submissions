class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = []
        while True:
            currnet_char = strs[0][i]
            print(currnet_char)
            for s in strs:
                if currnet_char == s[i]:
                    continue
                else:
                    return "".join(ans)
            ans.append(currnet_char)
            i += 1 

