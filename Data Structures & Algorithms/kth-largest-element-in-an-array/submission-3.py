class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # BF
        nums.sort()
        return nums[-k]
