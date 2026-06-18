class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        suffix = []
        for i in range(1,len(nums)):
            prd = 1
            ref = i-1
            while ref>=0:
                prd = prd*nums[ref]
                ref-=1
            prefix.append(prd)
        for i in range(0,len(nums)):
            prd = 1
            ref = i+1
            while ref<len(nums):
                prd = prd*nums[ref]
                ref+=1
            suffix.append(prd)
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans