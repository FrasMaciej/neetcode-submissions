class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # BF
        sorted_nums = nums
        sorted_nums.sort()
        return sorted_nums[-k]
