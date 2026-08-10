class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)-1
        l,r = 0, n
        maxvol = 0
        while l<r:
            maxvol = max(maxvol,(r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:                
                l+=1
            else:
                r-=1
        return maxvol