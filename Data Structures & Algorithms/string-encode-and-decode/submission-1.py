from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: <length>#<string>
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            # Find the position of the separator '#'
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            if j == len(s):
                raise ValueError("Invalid encoded string: missing '#' separator.")

            # Extract the length of the next string
            try:
                length = int(s[i:j])
            except ValueError:
                raise ValueError(f"Invalid length value: '{s[i:j]}'")

            # Move past the '#'
            i = j + 1

            # Extract the string of given length
            if i + length > len(s):
                raise ValueError("Invalid encoded string: length exceeds remaining characters.")
            res.append(s[i:i+length])

            # Move to the next encoded segment
            i += length
        return res
