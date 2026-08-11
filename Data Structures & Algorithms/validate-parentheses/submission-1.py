class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validPairs = {'()', '[]', '{}'}

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack.pop() + char not in validPairs:
                    return False
        return not stack