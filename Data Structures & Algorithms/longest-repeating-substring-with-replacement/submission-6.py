class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # define the hash map to store character freqs
        hashMap = {}

        # define result variable
        res = 0

        # define maxF to optimize tracking of max value of char freq
        maxF = 0

        # define left boundary of window
        l = 0

        # iterate through string
        for r in range(len(s)):
            # update frequency of current char
            hashMap[s[r]] = 1 + hashMap.get(s[r],0)

            # update maxF if current char has max freq
            maxF = max(maxF, hashMap[s[r]])

            # check if chars to change is greater than number of 
            # allowed replaces
            while (r - l + 1 ) - maxF > k:
                # decrement the frequency of the current char
                hashMap[s[l]] -= 1
                # increment the left boundary
                l += 1
            
            # keep track of longest substring
            res = max(res, (r - l + 1))
        return res
