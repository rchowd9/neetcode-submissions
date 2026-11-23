from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # Define operations
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)  # truncates toward zero
        }

        for token in tokens:
            if token in op:
                # Pop two operands (note: order matters for subtraction/division)
                b = stack.pop()
                a = stack.pop()
                stack.append(op[token](a, b))
            else:
                # Push numeric value
                stack.append(int(token))

        return stack.pop()
