class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [n for row in matrix for n in row]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_num = (l+r) // 2
            if nums[mid_num] == target:
                return True
            elif nums[mid_num] < target:
                l = mid_num + 1
            else:
                r = mid_num - 1
        return False