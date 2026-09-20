class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        numList = []

        # use currSum to store sum value as using sum() increases
        # time complexity from O(2^n) to O(k*2^n)

        def dfs(i, currSum):
            if currSum == target:
                res.append(numList.copy())
                return
            
            for j in range(i,len(nums)):
                if currSum + nums[j] > target:
                    break
                numList.append(nums[j])
                dfs(j, currSum + nums[j])
                numList.pop()
            
        dfs(0,0)
        return res

            