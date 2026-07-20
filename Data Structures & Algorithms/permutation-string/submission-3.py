class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        cs1,cs2 = [0]*26,[0]*26
        for i in range(len(s1)):
            cs1[ord(s1[i])-ord('a')]+=1
            cs2[ord(s2[i])-ord('a')]+=1
        matches = 0
        for i in range(26):
            if cs1[i]==cs2[i]:
                matches+=1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            ind = ord(s2[r])-ord('a')
            cs2[ind]+=1
            if cs1[ind] == cs2[ind]:
                matches+=1
            elif cs1[ind]+1 == cs2[ind]:
                matches -= 1
            ind = ord(s2[l])-ord('a')
            cs2[ind]-=1
            if cs1[ind]==cs2[ind]:
                matches+=1
            elif cs1[ind]-1==cs2[ind]:
                matches -=1
            l+=1
        return matches == 26