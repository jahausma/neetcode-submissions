class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # key point is that in order for a car behind another car to join a fleet, 
        # the time to the destination of it must be shorter than the car in front 

        # time = (target - position)/speed

        # NOTE: we must sort cars first, we should look at the cars closest to the
        # target first

        list_sort = [(p,s) for p,s in zip(position, speed)]  # create a list of tuples

        list_sort.sort(reverse=True)

        # we can use a stack to keep track of what cars have joined fleets

        stack = []  # time of car ahead
        num_fleets = 0 # tracks number of fleets

        # note that a car can not pass a car, only match its speed.
        for p,s in list_sort:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
