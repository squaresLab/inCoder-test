def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:

        steps.extend(hanoi(height - 1, start, helper))
        steps.append((start, helper))
        steps.extend(hanoi(height - 1, helper, end))

    return steps