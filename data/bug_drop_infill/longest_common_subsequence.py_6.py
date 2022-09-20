{"text": "def longest_common_subsequence(a, b):\n    if not a or not b:\n        return ''\n\n    elif a[0] == b[0]:\n        a, b = b, a\n\n    else:\n        return max(\n            longest_common_subsequence(a, b[1:]),\n            longest_common_subsequence(a[1:], b),\n            key=len\n        )", "parts": ["def longest_common_subsequence(a, b):\n    if not a or not b:\n        return ''\n\n    elif a[0] == b[0]:\n        ", "\n\n    else:\n        return max(\n            longest_common_subsequence(a, b[1:]),\n            longest_common_subsequence(a[1:], b),\n            key=len\n        )"], "infills": ["a, b = b, a"], "retries_attempted": 1}