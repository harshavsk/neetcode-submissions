class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maps = {}
        l = 0
        maxsize = 0
        maxf = 0
        for r in range(len(s)):
            maps[s[r]]= 1+maps.get(s[r],0)
            maxf = max(maxf,maps[s[r]])
            while (r-l+1)-maxf>k:
                maps[s[l]]-=1
                l+=1
            maxsize = max(maxsize,(r-l+1))
        return maxsize