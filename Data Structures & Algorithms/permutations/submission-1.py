class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the number of permutations equals n!
        # number of subsets equals 2^n

        # base case
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res = []

        for p in perm:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                print(p_copy)
                res.append(p_copy)

        return res
