from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_products = [1] * length
        suffix_products = [1] * length
        result = [0] * length

        # Compute prefix products
        for i in range(1, length):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]

        # Compute suffix products
        for i in range(length - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]

        # Compute result
        for i in range(length):
            result[i] = prefix_products[i] * suffix_products[i]

        return result