class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # BF: check all combinations and return max 
        n, res = len(nums), nums[0]

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                res = max(curr_sum, res)

        return res

