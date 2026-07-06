# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLen = 0
#         for i in range(0,len(s)):
#             words = set()
#             r=i
#             while r<len(s):
#                 if s[r] in words:
#                     break
#                 words.add(s[r])
#                 maxLen = max(maxLen,len(words))
#                 r+=1
#         return maxLen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        words = set()
        for r in range(len(s)):
            while s[r] in words:
                words.remove(s[l])
                l+=1
            words.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen