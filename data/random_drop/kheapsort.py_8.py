def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr:


    while heap:
        yield heapq.heappop(heap)