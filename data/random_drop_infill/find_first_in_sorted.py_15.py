{"text": "def find_first_in_sorted(arr, x):\n    lo = 0\n    hi = len(arr)\n\n    while lo <= hi:\n        mid = (lo + hi) // 2\n\n        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):\n            return mid\n\n        elif x <= arr[mid]:\n            hi = mid\n\n        else:\n            lo = mid + 1\n\n    return -1", "parts": ["def find_first_in_sorted(arr, x):\n    lo = 0\n    hi = len(arr)\n\n    while lo <= hi:\n        mid = (lo + hi) // 2\n\n        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):\n            return mid\n\n        elif x <= arr[mid]:\n            hi = mid\n\n        else:\n            ", "\n\n    return -1"], "infills": ["lo = mid + 1"], "retries_attempted": 1}