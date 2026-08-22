class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base Case: check for empty string
        if t == "": return ""

        countT, window = {}, {}

        # initialize countT map
        for c in t:
            countT[c] = 1 + countT.get(c,0) # safe in case there is not an element yet
        
        # use to keep track of conditional arguments 
        have, need = 0, len(countT)

        # initialize values for keeping track of results
        res, resLen = [-1,-1], float("infinity")
        # initialize left pointer
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            # updating window
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l +1)
                    # pop from the left of our window maps
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # incrementing left pointer
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
