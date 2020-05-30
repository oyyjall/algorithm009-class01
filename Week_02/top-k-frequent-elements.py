from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        dic = defaultdict(int)
        res = []
        for i in range(0, len(nums)):
            dic[nums[i]] += 1
        alist = sorted(dic.items(), key = lambda item:item[1]  , reverse = True)
        for i in range(0, k):
            res.append(alist[i][0])
        return res