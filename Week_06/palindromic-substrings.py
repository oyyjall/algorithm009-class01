class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1.动态规划
        if not s:
            return 0
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        res = 0
        for j in range(0, len(s)):
            for i in range(0, j+1):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res

        # 2.中心扩展法
        if not s:
            return 0
        res = 0
        for center in range(0, 2*len(s)-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res