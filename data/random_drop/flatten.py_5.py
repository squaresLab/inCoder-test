def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):

        else:
            yield flatten(x)