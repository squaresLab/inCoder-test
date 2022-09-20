def bitcount(n):
    count = 0
    <insert>
        n ^= n - 1
        count += 1
    return count