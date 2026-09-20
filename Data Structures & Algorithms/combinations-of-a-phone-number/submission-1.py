class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        path = []
        digit_letter_map = {
                "2":"abc", "3":"def", "4":"ghi",
                "5":"jkl", "6":"mno", "7":"pqrs", 
                "8":"tuv", "9":"wxyz"
            }

        def dfs(start_index):
            # base case
            if start_index == len(digits):
                res.append("".join(path[:]))
                return
            
            # choices
            # - digits 2 to 9, depending on the digits i 
            # - need generate all possible combinations of the letters
            current_digit = digits[start_index]
            letters_pool = digit_letter_map[current_digit]
            for letter in letters_pool:
                path.append(letter)
                dfs(start_index+1)
                path.pop()

        dfs(0)
        return res        

        
