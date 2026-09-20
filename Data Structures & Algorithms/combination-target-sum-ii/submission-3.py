class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        numList = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(numList.copy())
                return
            elif i == len(candidates) or currSum > target:
                return
            
            # include the current candidate
            numList.append(candidates[i])
            dfs(i+1,currSum + candidates[i])
            numList.pop()

            # exclude the current candidate
            # [1,1,1,1,2] 
            # [1,1,1,1] -> must check that i+1<len(candidates)
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,currSum)

        dfs(0,0)
        return res