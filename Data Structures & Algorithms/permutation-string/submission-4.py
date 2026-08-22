class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check for base case immediately (s1 > s2)
        if len(s1) > len(s2):
            return False

        # we want to allocate two static arrays for s1 and s2 counts
        s1Count = [0] * 26
        s2Count = [0] * 26

        # initialize the initial counts of both s1 and s2
        for i in range(len(s1)):
            # index into s1 and s2 by converting chars to ascii values
            # increment the count
            s1Count[ord(s1[i])- ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # initialize matches variable that keeps track of the 
        matches = 0
        
        # find the number of matches originally
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # initialize the left boundary
        l = 0
        # iterate over the elements that s2 has and s1 doesn't
        for r in range(len(s1), len(s2)):
            # check if matchest = 26 and return if yes
            if matches == 26: return True

            # grab the current index at right boundary
            index = ord(s2[r]) - ord('a')
            # increment that index's freq count
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # grab index at left boundary
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

        


            