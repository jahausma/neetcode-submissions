class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # O(nlogn)
        intervals.sort(key = lambda i : i[0]) # sort them in ascending order at first

        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
                # [1,5], [2,4] = [1,5]
            else:
                output.append([start, end]) # non overlapping, result is itself
                # [1,5], [7,8] = [1,5], [7,8]
            
        return output