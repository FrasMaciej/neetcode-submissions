class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        temp_len = len(temperatures)

        for i in range (temp_len):
            while stack and temperatures[i] > stack[-1][0]:
                stack_top = stack.pop()
                result[stack_top[1]] = i - stack_top[1]
            stack.append((temperatures[i], i))

        return result