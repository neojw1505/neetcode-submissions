class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping_dict = collections.defaultdict(list)
        for s in strings:
            if len(s) == 1:
                grouping_dict[(-1,)].append(s)
            else:
                diff_chars = []
                for i in range(1, len(s)):
                    diff = (ord(s[i]) - ord(s[i-1])) % 26   
                    diff_chars.append(diff)
                grouping_dict[tuple(diff_chars)].append(s)
        return list(grouping_dict.values())