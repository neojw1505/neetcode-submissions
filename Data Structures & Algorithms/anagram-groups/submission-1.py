class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for string in strs:
            # create a key for each str
            key = [0] * 26 
            # loop each ch in str 
            for ch in string:
                ascii_val = ord(ch) % 26 # get the ascii value
                key[ascii_val] += 1 # increase freq for that char

            # need to change to tuple as immutable
            # list is not immutable
            key = tuple(key)
            # use the unique key to form a key in hashmap
            # value should be a list
            if not m.get(key):
                m[key] = []
            m[key].append(string) 
        
        # empty list res
        res = []
        for v in m.values():
            res.append(v)
        return res
            