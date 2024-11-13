class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_map = {0: 1}  # Initialize with 0 remainder having one count
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Normalize negative remainders
            if remainder < 0:
                remainder += k
            
            # If remainder already exists in map, add its count to the result
            if remainder in remainder_map:
                count += remainder_map[remainder]
                remainder_map[remainder] += 1
            else:
                remainder_map[remainder] = 1
        
        return count
