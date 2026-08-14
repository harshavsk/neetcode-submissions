class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        mp1,mp2 = [0]*26, [0]*26
        matches = 0
        for i in range(len(s1)):
            mp1[ord(s1[i])-ord('a')]+=1
            mp2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if mp1[i]==mp2[i]:
                matches+=1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            ind = ord(s2[r])-ord('a')
            mp2[ind]+=1
            if mp1[ind]==mp2[ind]:
                matches+=1
            elif mp1[ind]+1==mp2[ind]:
                matches-=1
            ind = ord(s2[l])-ord('a')
            mp2[ind]-=1
            if mp1[ind]==mp2[ind]:
                matches+=1
            elif mp1[ind]-1==mp2[ind]:
                matches-=1
            l+=1
        return matches==26