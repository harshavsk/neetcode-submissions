class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        for i in range(n+1):
            while stack and (i==n or heights[i]<heights[stack[-1]]):
                ind = stack.pop()
                height = heights[ind]
                maxArea = max(maxArea,height*(i-stack[-1]-1 if stack else i))
            stack.append(i)
        return maxArea