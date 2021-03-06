#!/usr/bin/python3
"""
    Rain
"""


def rain(walls):
    """
    Method to calculate how many square units of water will be retained after
    it rains.
    Parameters:
        walls: (list) non-negative integers.
    Returns:
        Integer indicating total amount of rainwater retained.
    """
    n = len(walls)

    if n == 0:
        return 0

    # To store the maximum water
    # that can be stored
    res = 0

    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        # Find the maximum element on its right
        right = walls[i]

        for j in range(i + 1, n):
            right = max(right, walls[j])

        # Update the maximum water
        res = res + (min(left, right) - walls[i])

    return res
