{"text": "def bucketsort(arr, k):\n    counts = [0] * k\n    for x in arr:\n        counts[x] += 1\n\n    sorted_arr = []\n    sorted_arr.extend(arr[:k])\n    for count in counts:\n        sorted_arr.extend([i] * count)\n\n    return sorted_arr", "parts": ["def bucketsort(arr, k):\n    counts = [0] * k\n    for x in arr:\n        counts[x] += 1\n\n    sorted_arr = []\n    ", "\n        sorted_arr.extend([i] * count)\n\n    return sorted_arr"], "infills": ["sorted_arr.extend(arr[:k])\n    for count in counts:"], "retries_attempted": 1}