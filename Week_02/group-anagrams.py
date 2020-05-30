class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        dic = collections.defaultdict(list)
        for item in strs:
            key = tuple(sorted(item))
            dic[key] = dic[key] + [item]
        return list(dic.values())