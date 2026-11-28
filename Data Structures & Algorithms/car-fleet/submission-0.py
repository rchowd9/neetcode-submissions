from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Calculates the number of car fleets that will arrive at the target.
        
        A fleet is formed when a faster car catches up to a slower car before reaching the target.
        Once cars join a fleet, they travel together at the slowest fleet speed.
        
        Args:
            target (int): The destination position.
            position (List[int]): Positions of cars.
            speed (List[int]): Speeds of cars.
        
        Returns:
            int: Number of fleets that reach the target.
        """
        
        # Input validation
        if not isinstance(target, int) or target <= 0:
            raise ValueError("Target must be a positive integer.")
        if len(position) != len(speed):
            raise ValueError("Position and speed lists must have the same length.")
        if any(p < 0 or p > target for p in position):
            raise ValueError("Car positions must be between 0 and target.")
        if any(s <= 0 for s in speed):
            raise ValueError("Car speeds must be positive.")

        # Pair each car's position with its time to reach target
        cars = sorted(zip(position, speed), reverse=True)  # Sort by position descending
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        prev_time = 0.0

        # Iterate over cars from closest to target to farthest
        for t in times:
            # If this car's time is greater than the previous fleet's time,
            # it forms a new fleet
            if t > prev_time:
                fleets += 1
                prev_time = t

        return fleets


# Example usage
if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print("Number of fleets:", sol.carFleet(target, position, speed))
