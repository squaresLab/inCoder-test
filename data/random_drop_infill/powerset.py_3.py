{"text": "def powerset(arr):\n    if arr:\n        first = arr[0]\n        rest_subsets = powerset(rest)\n        return [[first] + subset for subset in rest_subsets]\n    else:\n        return [[]]", "parts": ["def powerset(arr):\n    if arr:\n        ", "\n        rest_subsets = powerset(rest)\n        return [[first] + subset for subset in rest_subsets]\n    else:\n        return [[]]"], "infills": ["first = arr[0]"], "retries_attempted": 1}