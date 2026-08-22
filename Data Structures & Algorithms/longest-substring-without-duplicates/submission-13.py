class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can use sliding window for this problem to keep
        # track of duplicates found 
        l = 0

        # use a set to keep track of seen elements
        unique_set = set()
        longest_length = 0
        
        for r in range(len(s)):
            while s[r] in unique_set:
                unique_set.remove(s[l])
                l +=1
            unique_set.add(s[r])
            longest_length = max(longest_length, r - l + 1)

        return longest_length
