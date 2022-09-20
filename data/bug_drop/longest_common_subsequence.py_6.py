def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        <insert>

    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len
        )