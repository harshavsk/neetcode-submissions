class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        n = len(heights)
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>heights[i]):
                height = heights[stack.pop()]
                width = i-1-stack[-1] if stack else i
                area = max(area,height*width)
            stack.append(i)
        return area