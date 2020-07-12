class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            res ^= 1 << (31 - i) if n & (1 << i) != 0 else 0
        return res