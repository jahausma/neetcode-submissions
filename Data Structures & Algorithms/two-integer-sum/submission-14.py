class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can use a hash map to store the number in the input as well as the difference that would add up to 7
        res = []
        hashMap = {} # pair: actual number, index

        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in hashMap:
                res.append(hashMap[difference])
                res.append(i)
                return res
            hashMap[nums[i]] = i
        
