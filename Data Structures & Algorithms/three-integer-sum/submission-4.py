class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        ans = []
        # iterate through each number and then use a while loop to iterate from each end
        # we start the two pointers in the while loop from the i+1 and end
        for i,a in enumerate(nums):

            if a > 0:
                break # we dont need to evaluate positives as adding positives will never = 0

            if i > 0 and a == nums[i-1]: # this prevents duplicate lists being appended
                continue

            l,r = i + 1, len(nums) - 1

            while l < r:
                tempSum = a + nums[l] + nums[r]
                if tempSum > 0:
                    r -=1
                elif tempSum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans