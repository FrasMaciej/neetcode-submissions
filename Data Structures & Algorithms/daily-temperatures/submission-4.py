class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 <= temperatures[i] <= 100
        # 1 <= temperatures.length <= 1000  
        # result = []
        # cycle:       
        # append temperatures[n] to stack
        # pop all from the stack and for these smaller than current => pop and save number to result
        # add current to stack
        # repeat
        
        # temp_len = len(temperatures)
        # for i in range (temp_len - 1):
        #     for j in range (i+1, temp_len):
        #         if temperatures[j] > temperatures[i]:
        #             result.append(j-i)
        #             break
        #         elif j == temp_len - 1:
        #             result.append(0)
        # result.append(0)

        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        temp_len = len(temperatures)

        for i in range (1, temp_len):
            while stack and temperatures[i] > stack[-1][0]:
                stack_top = stack.pop()
                result[stack_top[1]] = i - stack_top[1]
            stack.append((temperatures[i], i))

        return result