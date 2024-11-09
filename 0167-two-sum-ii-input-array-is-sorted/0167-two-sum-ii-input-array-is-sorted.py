class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            n = target-numbers[i]
            if n in hashmap:
                return [hashmap[n]+1,i+1]
            hashmap[numbers[i]] = i
        return []