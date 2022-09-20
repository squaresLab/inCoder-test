def subsequences(a, b, k):
    <insert>
        return []

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret