class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_index = (l + r) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                r = mid_index - 1
            else:
                l = mid_index + 1
        return -1