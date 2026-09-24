class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Multiplying anything by zero results in zero
        if num1 == "0" or num2 == "0":
            return "0"

        LEN_1 = len(num1)
        LEN_2 = len(num2)

        result = [0] * (LEN_1 + LEN_2)

        # Scan from right-to-left
        for i in range(LEN_1 - 1, -1, -1):
            for j in range(LEN_2 - 1, -1, -1):
                
                # Convert text characters to single mathematical integers safely 
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                raw_product = digit1 * digit2

                target_slot = i + j + 1
                carry_slot = i + j

                total_sum = raw_product + result[target_slot]
                
                digit_in_target_slot = total_sum % 10
                digit_in_carry_slot = total_sum // 10

                result[target_slot] = digit_in_target_slot
                result[carry_slot] += digit_in_carry_slot


        # Since we pre-allocated size, only index 0 can possibly be an empty placeholder 0!
        start_index = 1 if result[0] == 0 else 0

        return "".join([str(digit) for digit in result[start_index:]])
