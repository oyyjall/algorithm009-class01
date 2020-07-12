from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        dic = Counter(arr1)
        res = []
        for num in arr2:
            while dic[num] > 0:
                res.append(num)
                dic[num] -= 1

        for i in range(0, len(arr1)):
            while dic[arr1[i]] > 0:
                res.append(arr1[i])
                dic[arr1[i]] -= 1
        return res