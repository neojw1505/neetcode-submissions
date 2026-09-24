class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            # last digit not 9
            if digits[i] < 9:
                digits[i] += 1
                return digits

            while carry:
                digits[i] += carry
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
                carry -= 1

            # last digit is 9
            if digits[i] == 9:
                digits[i] = 0

        return [1] + digits