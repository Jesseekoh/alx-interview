#!/usr/bin/python3
"""0-minoperations module"""


def minoperations(n):
    """computes the minimum number of operations needed to result
     in exactly n H characters"""
    if type(n) is not int:
        return 0
    opsCount = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            opsCount += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            opsCount += 2
        elif clipboard > 0:
            done += clipboard
            opsCount += 1
    return opsCount
