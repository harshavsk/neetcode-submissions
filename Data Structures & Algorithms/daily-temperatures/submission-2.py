class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                t,ind = stack.pop()
                res[ind] = i-ind
            stack.append((temp,i))
        return res