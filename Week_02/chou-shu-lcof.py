class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        a, b, c = 0, 0, 0
        res = [1] * n
        for i in range(1, n):
            res[i] = min(res[a]*2, res[b]*3, res[c]*5)
            if res[i] == res[a]*2:
                a += 1
            if res[i] == res[b]*3:
                b += 1
            if res[i] == res[c]*5:
                c += 1
        return res[-1]