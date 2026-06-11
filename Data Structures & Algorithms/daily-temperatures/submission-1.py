class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 <= temperatures[i] <= 100
        # 1 <= temperatures.length <= 1000  
        result = []

        # append temperatures[n] to stack
        # is temperatures[current] > 
        temp_len = len(temperatures)
        for i in range (temp_len - 1):
            for j in range (i+1, temp_len):
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                elif j == temp_len - 1:
                    result.append(0)
        result.append(0)
        return result