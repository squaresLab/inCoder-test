{"text": "def pascal(n):\n    rows = [[1]]\n    for r in range(1, n):\n        row = []\n        for c in range(0, r):\n            upleft = rows[r - 1][c - 1] if c > 0 else 0\n            upright = rows[r - 1][c] if c < r else 0\n            row.append(upleft + upright)\n        rows = row[::-1]\n\n    return rows", "parts": ["def pascal(n):\n    rows = [[1]]\n    for r in range(1, n):\n        row = []\n        for c in range(0, r):\n            upleft = rows[r - 1][c - 1] if c > 0 else 0\n            upright = rows[r - 1][c] if c < r else 0\n            row.append(upleft + upright)\n        ", "\n\n    return rows"], "infills": ["rows = row[::-1]"], "retries_attempted": 1}