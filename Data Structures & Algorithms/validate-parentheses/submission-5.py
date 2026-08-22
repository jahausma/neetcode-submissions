class Solution:
    def isValid(self, s: str) -> bool:

        list_opens = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for char in s:
            # check if c in closeToOpen
            if char in closeToOpen:
                # check if stack is not empty and the last element of stack is equal to the dictionary
                    # mapping of closeToOpen[char]
                if list_opens and list_opens[-1] == closeToOpen[char]:
                    list_opens.pop()
                else:
                    return False
            else:
                list_opens.append(char)

        if not list_opens:
            return True
        else: 
            return False