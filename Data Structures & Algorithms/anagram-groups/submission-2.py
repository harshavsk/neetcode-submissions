class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            mp = [0]*26
            for c in s:
                mp[ord(c)-ord('a')]+=1
            res[tuple(mp)].append(s)
        return list(res.values())