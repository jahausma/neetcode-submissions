class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in mp:
                mp.remove(s[l])
                l += 1
            mp.add(s[r])
            maxLength = max(maxLength, r - l + 1)
                
        return maxLength