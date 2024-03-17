#!/usr/bin/python3
"""0_lockboxes module"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys

    Returns:
        boolean: True if all boxes can be opened and False if not all can be
    """
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        boxIdx = unchecked_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[boxIdx])
            checked_boxes.add(boxIdx)
    return n == len(checked_boxes)
