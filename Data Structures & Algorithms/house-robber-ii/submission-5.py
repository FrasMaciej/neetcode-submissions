class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.calculate_subproblem(nums[1:]), self.calculate_subproblem(nums[:-1]))

    def calculate_subproblem(self, nums):
        prev, prev_prev = 0, 0
        for n in nums:
            temp = max(prev, prev_prev + n)
            prev_prev = prev
            prev = temp
        return prev

        
        