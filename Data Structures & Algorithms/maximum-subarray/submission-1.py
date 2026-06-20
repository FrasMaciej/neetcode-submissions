class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # BF: check all combinations and return max 
        i, j = 0, len(nums) - 1
        output = -99999999999999999
        for i in range (len(nums)):
            curr_sum = 0
            for j in range (i, len(nums)):
                curr_sum += nums[j]
                if curr_sum > output:
                    output = curr_sum 
        
        return output
