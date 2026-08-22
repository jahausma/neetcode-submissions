class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = -1
        index2 = -1
        for i in range(len(numbers)):
            if ((target - numbers[i]) in numbers) and index1 == -1:
                index1 = i
                second_num = target - numbers[i]
                print(index1)
                print(second_num)
            if index1 !=-1:
                if numbers[i] == second_num:
                    index2 = i
                    return [index1+1, index2+1]
        return []