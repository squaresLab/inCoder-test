def detect_cycle(node):
    hare = tortoise = node

    while True:

            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True