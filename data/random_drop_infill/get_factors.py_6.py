{"text": "def get_factors(n):\n    if n == 1:\n        return []\n\n    for i in range(2, int(n ** 0.5) + 1):\n        factors = []\n        while n % i == 0:\n            factors.append(i)\n            n //= i\n        if factors:\n            return [i] + get_factors(n // i)\n\n    return []", "parts": ["def get_factors(n):\n    if n == 1:\n        return []\n\n    for i in range(2, int(n ** 0.5) + 1):\n        ", "\n            return [i] + get_factors(n // i)\n\n    return []"], "infills": ["factors = []\n        while n % i == 0:\n            factors.append(i)\n            n //= i\n        if factors:"], "retries_attempted": 1}