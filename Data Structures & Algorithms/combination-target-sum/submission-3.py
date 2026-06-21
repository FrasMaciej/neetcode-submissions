class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination):
            if sum(combination) == target:
                res.append(combination.copy())
                return
            elif sum(combination) > target or i >= len(nums):
                return
            
            combination.append(nums[i])
            dfs(i, combination)
            combination.pop()
            dfs(i + 1, combination)

        
        dfs(0, [])
        return res