class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, nums_used, cur_permutation):
            if len(cur_permutation) == len(nums):
                res.append(cur_permutation.copy())
                return

            for i in range(len(nums)):
                if not nums_used[i]:
                    cur_permutation.append(nums[i])
                    nums_used[i] = True
                    backtrack(nums, nums_used, cur_permutation)
                    cur_permutation.pop()
                    nums_used[i] = False

        res = []
        backtrack(nums, [False] * len(nums), [])
        return res
        