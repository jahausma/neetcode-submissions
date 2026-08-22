class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        seen = set()
        if (nums[r] == nums[l]):
            return nums[r]

        while l <= r:
            if nums[r] in seen or nums[l] in seen:
                return nums[l] if nums[l] in seen else nums[r]
            seen.add(nums[r])
            seen.add(nums[l])
            print(nums[l])
            l +=1
            r -=1
        return nums[r] if nums[r] in seen else nums[l]