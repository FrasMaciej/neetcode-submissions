class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subarr, output):
            if not subarr:
                res.append(output.copy())
                return

            for n in subarr:
                next_output = output.copy()
                next_output.append(n)
                next_subarr = subarr.copy()
                next_subarr.remove(n)
                dfs(next_subarr, next_output) #do dfs without the element that was just used 


        dfs(nums, [])
        return res
        