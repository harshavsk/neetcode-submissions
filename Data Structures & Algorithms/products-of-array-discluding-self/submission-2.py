class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prd = 1
        for i in range(len(nums)):
            ans[i]=prd
            prd *= nums[i]
        prd = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= prd
            prd *= nums[i]
        return ans