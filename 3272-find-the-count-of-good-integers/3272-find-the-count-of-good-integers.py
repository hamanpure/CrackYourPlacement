from itertools import permutations
from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        from itertools import permutations

        def is_palindrome(s):
            return s == s[::-1]

        def is_valid(digits):
            """Check if the digit counts can be rearranged into a palindrome"""
            freq = Counter(digits)
            odd_count = sum(1 for v in freq.values() if v % 2 != 0)
            return odd_count <= 1

        def generate_all_unique_perms(digits):
            """Generate all unique permutations of digits without leading 0s"""
            perms = set()
            for p in permutations(digits):
                if p[0] != '0':
                    perms.add("".join(p))
            return perms

        from itertools import product

        total = 0
        # Generate all n-digit numbers (as strings with digits only)
        for comb in product("0123456789", repeat=n):
            if comb[0] == '0':
                continue  # no leading zeros
            if not is_valid(comb):
                continue  # can't make a palindrome

            unique_perms = generate_all_unique_perms(comb)

            for p in unique_perms:
                if is_palindrome(p) and int(p) % k == 0:
                    total += 1
                    break  # only one valid rearrangement is enough

        return total
