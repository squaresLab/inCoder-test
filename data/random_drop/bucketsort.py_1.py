
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(arr):
        sorted_arr.extend([i] * count)

    return sorted_arr