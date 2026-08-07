class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        lar = 0
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                height = heights[stack.pop()]
                lar = max(lar,(height*(i-stack[-1]-1 if stack else i)))                
            stack.append(i)
        return lar