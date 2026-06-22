class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur_combination = []
        candidates.sort()
        def backtrack(n, cur_sum):
            if cur_sum == target:
                res.append(cur_combination.copy())
                return
            elif cur_sum > target or n == len(candidates):
                return

            last_used_cand = -1
            for i in range(n, len(candidates)):
                if last_used_cand != candidates[i] and candidates[i] + cur_sum <= target:
                    cur_combination.append(candidates[i])
                    cur_sum += candidates[i]
                    backtrack(i + 1, cur_sum)
                    cur_sum -= candidates[i]
                    cur_combination.pop()
                    last_used_cand = candidates[i]

        backtrack(0, 0)
        return res