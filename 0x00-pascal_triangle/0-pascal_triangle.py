#!/usr/bin/python3

"""
Pascal Triangle module
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    res = [[1]]
    for i in range(n):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(res[-1] + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
