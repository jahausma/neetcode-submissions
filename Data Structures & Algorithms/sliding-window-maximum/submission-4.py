class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            # check if we have filled the first window
            if i >= k - 1:
                # lazily remove elements that are outside the window boundary
                # issue with this solution is we have to re-push elements from last window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                output.append(-heap[0][0]) # append the first value
        return output
