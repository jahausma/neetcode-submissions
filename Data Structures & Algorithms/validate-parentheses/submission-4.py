class Solution:
    def isValid(self, s: str) -> bool:

        list_opens = []
        char_dict = {"{":"}", "(":")", "[":"]"}

        if len(s) % 2 == 1:
            return False

        for char in list(s):
            if char in char_dict.keys():
                list_opens.append(char)
            elif char in char_dict.values():
                print(char)
                if list_opens:
                    print("hello")
                    if char == "}" and list_opens[-1] != "{":
                        return False
                    if char == "]" and list_opens[-1] != "[":
                        return False
                    if char == ")" and list_opens[-1] != "(":
                        return False
                    list_opens.pop()
                else:
                    return False
        if not list_opens:
            return True
        else: 
            return False