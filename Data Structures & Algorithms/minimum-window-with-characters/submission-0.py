class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        smap,tmap = {},{}
        for c in t:
            tmap[c]=1+tmap.get(c,0)
        have,need = 0,len(tmap)
        res,reslen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            smap[c]=1+smap.get(c,0)
            if c in tmap and smap[c]==tmap[c]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    reslen = r-l+1
                    res = [l,r]
                smap[s[l]]-=1
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!= float("infinity") else ""