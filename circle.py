#!/usr/bin/env python3
"""
This is a sample script that demonstrates PEP 8 compliant code.
"""

import math


class Circle:
    """
    Represents a circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


def main():
    """
    The main function.

    Creates a Circle instance, calculates and prints its area and circumference.
    """
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"Area: {circle.area()}")
    print(f"Circumference: {circle.circumference()}")


if __name__ == "__main__":
    main()
