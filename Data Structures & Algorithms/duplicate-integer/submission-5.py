class Solution:      
    def hasDuplicate(self, nums: List[int]) -> bool:
        # BRUTE FORCE
        # j = 0
        # for i in nums:
        #     j+=1
        #     nums_shortened = nums[j:]
        #     if i in nums_shortened:
        #         return True

        # SORT FIRST
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        # return False

        memo = {}
        for num in nums:
            if num in memo:
                return memo[num]
            else: 
                memo[num] = True
        
        return False

        # Recursion slow
        # if not nums:
        #     return False
        # current = nums[0]
        # if current in nums[1:]:
        #     memo[current] = True
        #     return memo
        # if nums[0] == nums[-1]:
        #     return False
        # return self.hasDuplicate(nums[1:])