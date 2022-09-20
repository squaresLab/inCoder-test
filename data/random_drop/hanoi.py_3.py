def hanoi(height, start=1, end=3):
    steps = []
    <insert>
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        steps.append((start, helper))
        steps.extend(hanoi(height - 1, helper, end))

    return steps