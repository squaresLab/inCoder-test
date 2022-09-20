def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    <insert>
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)