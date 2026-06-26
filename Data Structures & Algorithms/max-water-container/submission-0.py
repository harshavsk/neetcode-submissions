class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxVolume = 0
        while l<r:
            maxVolume = max(maxVolume,(r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxVolume