class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(0,len(s)):
            words = set()
            r=i
            while r<len(s):
                if s[r] in words:
                    break
                words.add(s[r])
                maxLen = max(maxLen,len(words))
                r+=1
        return maxLen