{"text": "def powerset(arr):\n    if arr:\n        first, *rest = arr #python3 just like car and cdr (in this case anyway..)\n        rest_subsets = powerset(rest)\n        subsets = [first] + rest_subsets\n        return subsets\n    else:\n        return [[]]", "parts": ["def powerset(arr):\n    if arr:\n        first, *rest = arr #python3 just like car and cdr (in this case anyway..)\n        rest_subsets = powerset(rest)\n        ", "\n    else:\n        return [[]]"], "infills": ["subsets = [first] + rest_subsets\n        return subsets"], "retries_attempted": 1}