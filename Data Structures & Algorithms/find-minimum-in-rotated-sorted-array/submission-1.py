class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_n = 1001
        for n in nums:
            if n < min_n:
                min_n = n
        return min_n
