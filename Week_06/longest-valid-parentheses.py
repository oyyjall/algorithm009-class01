class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        res = 0
        for i in range(0, len(s)):
            if s[i] == ')' and stack[-1] >= 0 and s[stack.pop()] == '(':
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res