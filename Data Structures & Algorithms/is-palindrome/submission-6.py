import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ''.join([char for char in s if char not in string.punctuation])
        clean_s = clean_s.replace(" ", "")

        if len(clean_s) <= 1:
            return True
        left = clean_s[0]
        right = clean_s[-1]
        i = 0

        if len(clean_s) % 2 == 1:
            while i < len(clean_s)/2:
                print(f"left = {left}")
                print(f"right {right}")
                print(len(clean_s))
                if left.lower() == right.lower():
                    i +=1
                    left = clean_s[i]
                    right = clean_s[len(clean_s) - i -1]
                else:
                    return False
        else:
             while i < len(clean_s)/2:
                if left.lower() == right.lower():
                    i +=1
                    left = clean_s[i]
                    right = clean_s[len(clean_s) - i -1]
                    print(f"left = {left}")
                    print(f"right {right}")
                    print(len(clean_s))
                else:
                    return False
        
        return True
        