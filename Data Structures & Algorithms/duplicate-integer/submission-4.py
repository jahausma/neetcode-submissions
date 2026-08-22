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

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        # return False

        # Recursion
        if not nums:
            return False
        current = nums[0]
        if current in nums[1:]:
            memo[current] = True
            return memo
        if nums[0] == nums[-1]:
            return False

        return self. hasDuplicate(nums[1:])