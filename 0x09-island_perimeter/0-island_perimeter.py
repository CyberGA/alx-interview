#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    :param grid: List of lists representing the grid.
    :return: Integer representing the perimeter of the island.
    """
    perimeter = 0

    # Traverse rows and columns
    for row in grid + list(map(list, zip(*grid))):
        # Compare each cell with its next neighbor (including boundary with 0)
        for i1, i2 in zip([0] + row, row + [0]):
            if i1 != i2:
                perimeter += 1

    return perimeter
