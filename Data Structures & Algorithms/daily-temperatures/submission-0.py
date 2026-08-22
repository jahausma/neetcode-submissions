class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # we start by initilizing a list of zeros that is the length of temperatures
        list_result = [0] * len(temperatures)

        # we can use a stack to keep track of how many days until the next warmer day
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                list_result[stackInd] = i - stackInd
            stack.append((t,i))

        return list_result