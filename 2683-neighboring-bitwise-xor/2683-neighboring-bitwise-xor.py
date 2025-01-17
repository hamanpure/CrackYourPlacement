class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0

        for num in derived:
            if num:
                last = ~last
        return first == last