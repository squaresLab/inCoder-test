{"text": "def lis(arr):\n    ends = {}\n    longest = 0\n\n    for i, val in enumerate(arr):\n\n        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]\n\n        length = max(prefix_lengths) if prefix_lengths else 0\n\n        if length == longest or val < arr[ends[length + 1]]:\n            ends[length + 1] = i\n            longest = length\n\n    return ends\n\n    return longest", "parts": ["def lis(arr):\n    ends = {}\n    longest = 0\n\n    for i, val in enumerate(arr):\n\n        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]\n\n        length = max(prefix_lengths) if prefix_lengths else 0\n\n        if length == longest or val < arr[ends[length + 1]]:\n            ends[length + 1] = i\n            ", "\n\n    return longest"], "infills": ["longest = length\n\n    return ends"], "retries_attempted": 1}