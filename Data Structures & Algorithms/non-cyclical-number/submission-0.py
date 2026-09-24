class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digits(num):
            summ = 0
            while num:
                last_digit = num % 10
                num = num // 10 
                summ += last_digit**2
            return summ

        slow, fast = n, sum_digits(n)
        while slow != fast:
            slow = sum_digits(slow)
            fast = sum_digits(sum_digits(fast))
        
        return slow == fast == 1
            


       