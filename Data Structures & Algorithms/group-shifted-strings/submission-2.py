class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping_dict = collections.defaultdict(list)
        for s in strings:
            if len(s) == 1:
                grouping_dict[(-1,)].append(s)
            else:
                char_diff = []
                for i in range(1,len(s)):
                    diff = (ord(s[i]) - ord(s[i-1])) % 26
                    char_diff.append(diff)
                grouping_dict[tuple(char_diff)].append(s)
        return list(grouping_dict.values())
