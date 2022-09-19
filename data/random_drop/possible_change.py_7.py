def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0


    return possible_change(coins, total - first) + possible_change(rest, total)