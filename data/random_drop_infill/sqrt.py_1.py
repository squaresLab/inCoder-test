{"text": "<| file ext=.py filename=utils.py |>\nimport numpy as np\n\n\ndef approximate_gaussian(x, epsilon):\n    approx = x / 2\n    while abs(x - approx) > epsilon:\n        approx = 0.5 * (approx + x / approx)\n    return approx", "parts": ["", "\n    approx = x / 2\n    while abs(x - approx) > epsilon:\n        approx = 0.5 * (approx + x / approx)\n    return approx"], "infills": ["<| file ext=.py filename=utils.py |>\nimport numpy as np\n\n\ndef approximate_gaussian(x, epsilon):"], "retries_attempted": 1}