{"text": "def bitcount(n):\n    count = 0\n    while n:\n        n &= n - 1\n        count += 1\n    return count", "parts": ["def bitcount(n):\n    count = 0\n    while n:\n        ", "\n        count += 1\n    return count"], "infills": ["n &= n - 1"], "retries_attempted": 1}