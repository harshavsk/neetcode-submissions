class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        aggVol = 0
        leftMax,rightMax = height[l],height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                aggVol += leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                aggVol += rightMax-height[r]
        return aggVol