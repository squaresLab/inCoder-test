def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    <insert>
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)
    else:
        return pivot