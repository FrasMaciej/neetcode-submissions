class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, l, r = 0, 1, len(nums) - 1
        seen = set()
        output = []
        nums.sort()
        while i <= len(nums) - 3:
            while l < r:
                tuple_vals = tuple([nums[i], nums[l], nums[r]])
                sum_nums = nums[i] + nums[l] + nums[r]
                if sum_nums == 0 and tuple_vals not in seen:
                    seen.add(tuple_vals)
                    output.append(list(tuple_vals))
                elif sum_nums < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
            l = i + 1
            r = len(nums) - 1
        return output


        