{"text": "import string\ndef to_base(num, b):\n    result = ''\n    alphabet = string.digits + string.ascii_uppercase\n    while num > 0:\n        i = num % b\n        num = num // b\n        result += alphabet[i]\n    return result", "parts": ["import string\ndef to_base(num, b):\n    result = ''\n    alphabet = string.digits + string.ascii_uppercase\n    while num > 0:\n        i = num % b\n        num = num // b\n        ", "\n    return result"], "infills": ["result += alphabet[i]"], "retries_attempted": 1}