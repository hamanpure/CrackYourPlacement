from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # O(n log n)
        queue = deque(nums)  # O(n)
        operations = 0
        
        while len(queue) > 1 and queue[0] < k:
            x = queue.popleft()  # Smallest element (O(1))
            y = queue.popleft()  # Second smallest element (O(1))
            
            new_val = min(x, y) * 2 + max(x, y)
            operations += 1
            
            # Insert new_val in the correct position (O(n) worst case, but O(1) amortized if appending)
            if not queue or new_val >= queue[-1]:
                queue.append(new_val)
            else:
                for i in range(len(queue)):  # O(n) worst case
                    if queue[i] > new_val:
                        queue.insert(i, new_val)
                        break
        
        return operations if queue[0] >= k else -1
