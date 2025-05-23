class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1
    
    def get_next(self, n : int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total