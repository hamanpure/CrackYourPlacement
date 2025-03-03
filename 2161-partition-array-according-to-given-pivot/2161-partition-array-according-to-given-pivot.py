class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left, right = [], []
        mid = []
        for i in nums:
            if i <pivot:
                left.append(i)
        for i in nums:
            if i == pivot:
                mid.append(i)

        for j in nums:
            if j > pivot:
                right.append(j)

        return left+mid+right
