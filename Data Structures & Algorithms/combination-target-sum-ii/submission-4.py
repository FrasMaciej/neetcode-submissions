class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_combination = []

        candidates.sort()

        def backtrack(idx, cur_sum):
            if cur_sum == target:
                res.append(cur_combination.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]: 
                    continue
                if candidates[i] + cur_sum > target:
                    break

                cur_combination.append(candidates[i])
                backtrack(i + 1, cur_sum + candidates[i])
                cur_combination.pop()

        backtrack(0, 0)
        return res