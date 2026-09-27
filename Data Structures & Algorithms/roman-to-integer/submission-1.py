class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map each Roman character to its absolute value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        total_sum = 0
        i = 0
        n = len(s)

        while i < n:
            # Look ahead: If the next two characters are a known combination, take it!
            if i + 1 < n and s[i] + s[i+1] in roman_map:
                total_sum += roman_map[s[i]+s[i+1]]
                i += 2  # Jump forward 2 steps since we consumed a pair
            else:
                total_sum += roman_map[s[i]]
                i += 1  # Jump forward 1 step normally
        return total_sum

    # T: O(n) S: O(1)