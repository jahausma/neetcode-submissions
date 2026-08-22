class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # define a dictionary
        count = {}
        # define the output result variable
        res = 0

        # initialize the left boundary of window
        l = 0
        
        # loop over string s
        for r in range(len(s)):
            # add to existing dictionary item or include it for
            # the first time (count.get(s[r], 0) returns 0 if item
            # is showing up for the first time)
            count[s[r]] = 1 + count.get(s[r], 0) # use key to get count

            # while condition to check if current window is greater than 
            # capable replacement times until window is valid
            while (r - l + 1) - max(count.values()) > k:
                # decrement count of current left value
                count[s[l]] -= 1
                # increase left to next value
                l += 1
            res = max(res, r - l + 1)
        
        return res

