class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_top = stack.pop()
                result[stack_top[1]] = i - stack_top[1]
            stack.append((t, i))
        return result