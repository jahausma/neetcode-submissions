class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        
        if len(nums) == 0:
            return longest_seq
        
        longest_seq = 1;
        current_seq = 1;

        nums.sort()
        print(nums)
        left = nums[0]
        temp = nums[0];

        print(left)

        for num in nums:
            print(left)
            print(num)
            if num == temp+1:
                current_seq +=1;
                if current_seq > longest_seq: 
                    longest_seq = current_seq
            elif num == temp:
                continue            
            else:
                current_seq = 1;
                left = num;
            temp = num

        return longest_seq
            