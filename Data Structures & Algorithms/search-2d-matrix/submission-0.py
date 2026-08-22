class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # we can solve this using two binary searches, the first one will search each list and see if
        # target is in the list. The second one will search the list that target has been found in

        left_list = 0
        right_list = len(matrix) - 1

        while left_list <=right_list:

            mid_list = left_list + (right_list - left_list)//2

            if target in matrix[mid_list]:

                l = 0
                r = len(matrix[mid_list]) - 1
                list_target = matrix[mid_list]
                while l <= r:
                    mid = (l + r)//2

                    if list_target[mid] == target:
                        return True
                    elif list_target[mid] < target:
                        l += 1
                    else: 
                        r -= 1

            elif max(matrix[left_list]) < target:
                left_list += 1
            else:
                right_list -= 1

        return False