class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        numList = []

        # use currSum to store sum value as using sum() increases
        # time complexity from O(2^n) to O(k*2^n)

        def getCombination(i, currSum):
            if currSum == target:
                res.append(numList.copy())
                return
            elif currSum > target:
                return
            elif i == len(nums):
                return
            
            # we can keep using the current number
            currSum += nums[i]
            numList.append(nums[i])
            getCombination(i,currSum)

            # we can exclude the current number
            currSum -= nums[i]
            numList.pop()
            getCombination(i+1,currSum)
        
        getCombination(0,0)
        return res

            