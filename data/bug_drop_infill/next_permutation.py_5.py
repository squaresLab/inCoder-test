{"text": "def next_permutation(perm):\n    for i in range(len(perm) - 2, -1, -1):\n        if perm[i] < perm[i + 1]:\n            for j in range(len(perm) - 1, i, -1):\n                perm[j], perm[i] = perm[i], perm[j]\n                    next_perm = list(perm)\n                    next_perm[i], next_perm[j] = perm[j], perm[i]\n                    next_perm[i + 1:] = reversed(next_perm[i + 1:])\n                    return next_perm", "parts": ["def next_permutation(perm):\n    for i in range(len(perm) - 2, -1, -1):\n        if perm[i] < perm[i + 1]:\n            for j in range(len(perm) - 1, i, -1):\n                ", "\n                    next_perm = list(perm)\n                    next_perm[i], next_perm[j] = perm[j], perm[i]\n                    next_perm[i + 1:] = reversed(next_perm[i + 1:])\n                    return next_perm"], "infills": ["perm[j], perm[i] = perm[i], perm[j]"], "retries_attempted": 1}