class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert strings in array into 1 string
        # formula: length of string + delimiter (#) + the string itself 
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # 4#neet5#codes
    
    def decode(self, s: str) -> List[str]:
        # decode the encoded string
        # 1. find position of delimiter
        # 2. find delimiter position, to the left of delimiter is the number
        # 3. to the right of the delimiter is the encoded string
        # 4. store all encoded string in res
        res = []
        i = 0 # keep track of character

        while i < len(s):
            j = i
            # move until found delimiter
            while s[j] != '#':
                j += 1

            # the length of the string after the delimiter 
            length = int(s[i:j])

            encoded_str = s[j + 1: j + 1 + length]
            res.append(encoded_str)
        
            # move the i pointer, to the next string
            i = j + 1 + length
        return res
        
