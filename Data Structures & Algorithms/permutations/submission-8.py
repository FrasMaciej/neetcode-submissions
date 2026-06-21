class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if(len(perm) == len(nums)):
            self.res.append(perm.copy())
            return

        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False

        # res = []
        # def dfs(subarr, output):
        #     if not subarr:
        #         res.append(output.copy())
        #         return

        #     for n in subarr:
        #         next_output = output.copy()
        #         next_output.append(n)
        #         next_subarr = subarr.copy()
        #         next_subarr.remove(n)
        #         dfs(next_subarr, next_output) 


        # dfs(nums, [])
        # return res
        