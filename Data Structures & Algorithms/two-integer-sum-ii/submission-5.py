class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if map[complement]:
                return [map[complement], i + 1]

            map[numbers[i]] = i + 1

        return []