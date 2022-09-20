def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr:
        yield heapq.heappushpop(heap, x)

    <insert>
        yield heapq.heappop(heap)