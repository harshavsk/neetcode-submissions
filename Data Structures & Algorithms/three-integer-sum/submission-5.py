class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)-1
        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, n
            while l<r:
                sums = a+nums[l]+nums[r]
                if sums<0:
                    l+=1
                elif sums>0:
                    r-=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans