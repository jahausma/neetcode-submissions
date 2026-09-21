class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array first to get duplicates together

        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return res
            
            # we include current index
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            # we exclude current index, must skip over repeats
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            dfs(i+1)
        
        dfs(0)
        
        return res
            