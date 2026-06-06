class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i_1 = 0
        i_2 = len(numbers) - 1
        while i_1 < i_2:
            nums_sum = numbers[i_1] + numbers[i_2] 
            if nums_sum == target:
                return [i_1 + 1, i_2 + 1]
            elif nums_sum > target:
                i_2 -= 1
            else:
                i_1 += 1
