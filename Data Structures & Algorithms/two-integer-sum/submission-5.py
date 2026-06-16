class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i,n in enumerate(nums):
            diff = target-n
            if diff in ans:
                return [ans[diff], i]
            ans[n] = i

        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         ans[nums[i]+nums[j]]=[i,j]
        # return ans[target]