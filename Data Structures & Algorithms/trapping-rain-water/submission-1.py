class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL = height[l]
        maxR = height[r]
        vols = 0
        while l<r:
            if height[l]<height[r]:
                l+=1
                maxL = max(maxL,height[l])
                vols += maxL-height[l]
            else:
                r-=1
                maxR = max(maxR,height[r])
                vols += maxR-height[r]
        return vols
