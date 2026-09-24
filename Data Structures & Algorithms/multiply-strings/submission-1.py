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

                # Calculate the raw product of the two single digits
                raw_product = digit1 * digit2

                # Look up the destination indices
                target_slot = i + j + 1
                carry_slot = i + j

                # Factor in any existing value already sitting in this slot
                total_sum = raw_product + result[target_slot]

                # Split total sum into local unit digit and carry values
                result[target_slot] = total_sum % 10 # Overwrite current target slot with remainder
                result[carry_slot] += total_sum // 10  # Accumulate carry over into left slot

                
        start_index = 0
        while start_index < len(result) and result[start_index] == 0:
            start_index += 1
        
        return "".join(str(digit) for digit in result[start_index:])