class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we make an array that stores tuples of positions and speeds
        list_cars = [(p,s) for p,s in zip(position, speed)]

        # we then sort them in descending order 
        list_cars.sort(reverse=True)
                
        # we now iterate through the list of cars
        # we calculate a time for each car and compare it to the time to target of the car infront
        stack = []

        for p,s in list_cars:
            stack.append((target - p)/s) # time calculation
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            