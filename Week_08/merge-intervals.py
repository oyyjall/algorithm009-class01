class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        for itera in intervals:
            if len(res) == 0 or res[-1][1] < itera[0]:
                res.append(itera)
            else:
                res[-1][1] = max(res[-1][1], itera[1])
        return res