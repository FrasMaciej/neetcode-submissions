class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buffer = []
        for token in tokens:   
            if token in ["+", "-", "*", "/"]: 
                if token == "+":
                    current_value = buffer.pop() + buffer.pop()
                elif token == "-":
                    a, b = buffer.pop(), buffer.pop()
                    current_value = b - a
                elif token == "*":
                    current_value = buffer.pop() * buffer.pop()
                elif token == "/":
                    a, b = buffer.pop(), buffer.pop()
                    current_value = int(float(b) / a)
                buffer.append(current_value)
            else:
                buffer.append(int(token))
        
        return buffer[0]