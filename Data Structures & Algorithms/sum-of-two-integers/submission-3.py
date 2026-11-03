class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Maximum positive 32-bit integer
        MAX = 0x7FFFFFFF

        # Mask to keep numbers within 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # Sum without carry
            # Carry shifted one position left
            a, b = (a ^ b) & mask, ((a & b) & mask) << 1

        # Handle negative numbers in Python
        return a if a <= MAX else ~(a ^ mask)