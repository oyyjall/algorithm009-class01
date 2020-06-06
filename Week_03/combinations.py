class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        self.res = []
        self.backtrack(n, k, [], 1)
        return self.res

    def backtrack(self, n, k, track, index):
        if len(track) == k:
            self.res.append(track.copy())
            return
        for i in range(index, n+1):
            track.append(i)
            self.backtrack(n, k, track, i+1)
            track.pop()