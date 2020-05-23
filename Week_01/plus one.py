class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        digits = [0 for i in range(n+1)]
        digits[0] = 1
        return digits