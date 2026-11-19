class MinStack:
    def __init__(self):
        """
        Initialize two stacks:
        - main_stack: stores all values
        - min_stack: stores the minimum value at each state
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Push value onto the stack.
        Also update min_stack if val is a new minimum.
        """
        self.main_stack.append(val)
        # If min_stack is empty or val <= current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from the stack.
        Also update min_stack if the popped value was the minimum.
        """
        if not self.main_stack:
            raise IndexError("Pop from empty stack")
        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Return the top element of the stack.
        """
        if not self.main_stack:
            raise IndexError("Top from empty stack")
        return self.main_stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        if not self.min_stack:
            raise IndexError("GetMin from empty stack")
        return self.min_stack[-1]


# Example usage
if __name__ == "__main__":
    stack = MinStack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(2)
    stack.push(1)
    print("Top:", stack.top())       # Output: 1
    print("Min:", stack.getMin())    # Output: 1
    stack.pop()
    print("Min after pop:", stack.getMin())  # Output: 2

