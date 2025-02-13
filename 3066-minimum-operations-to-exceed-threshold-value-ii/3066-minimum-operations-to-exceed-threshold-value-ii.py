import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return 0

        heapq.heapify(nums)
        
        count = 0
        print(nums)
        while nums[0] < k and len(nums)>1:
            x,y = heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y) )
            count+=1

        return count

