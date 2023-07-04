def canUnlockAll(boxes):
    # Create a set of all box numbers
    all_boxes = set(range(len(boxes)))

    # Create a set of unlocked boxes
    unlocked_boxes = set([0])

    # Loop through the unlocked boxes and add any new keys to the unlocked set
    while True:
        new_boxes = set()
        for box in unlocked_boxes:
            new_boxes.update(set(boxes[box]))
        new_unlocked_boxes = new_boxes.intersection(all_boxes) - unlocked_boxes
        if not new_unlocked_boxes:
            break
        unlocked_boxes.update(new_unlocked_boxes)

    # If all boxes are unlocked, return True, else return False
    return len(unlocked_boxes) == len(all_boxes)

