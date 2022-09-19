def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)


        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)