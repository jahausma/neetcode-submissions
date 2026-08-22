class Solution:
    def ceil_div(self,a, b):
        return -(-a // b)   

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # key points: Koko can only eat from one pile each hour. This means that len(piles) <= h
        # Worst case: k = the max number of bananas in a single pile (h = len(piles))
        
        # # BRUTE FORCE METHOD
        # speed = 1
        # while speed <= max(piles):
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)
            
        #     if totalTime <= h: 
        #         return speed
        #     speed +=1 
        # return speed

        # BINARY SEARCH METHOD

        # initialize left and right for BS
        left = 1
        right = max(piles)

        # we set res to the max at first
        res = right

        while left <= right:
            total_time = 0
            k = left + (right - left)//2

            for pile in piles:
                total_time += math.ceil(pile/k)
            
            if total_time <= h:
                res = min(res,k)
                right = k -1 # look for even smaller k
            else:
                left = k + 1 # look for bigger k
            
        return res

