{"text": "<| file source=github |>\nimport string\n\n\ndef to_int(num):\n    return int(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_\ndef to_base(num, b):\n    result = ''\n    alphabet = string.digits + string.ascii_uppercase\n    while num > 0:\n        i = num % b\n        num = num // b\n        result = result + alphabet[i]\n    return result", "parts": ["", "\ndef to_base(num, b):\n    result = ''\n    alphabet = string.digits + string.ascii_uppercase\n    while num > 0:\n        i = num % b\n        num = num // b\n        result = result + alphabet[i]\n    return result"], "infills": ["<| file source=github |>\nimport string\n\n\ndef to_int(num):\n    return int(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_binary(num):\n    return bin(num)\n\n\ndef to_decimal(num):\n    return decimal.Decimal(num)\n\n\ndef to_hex(num):\n    return hex(num)\n\n\ndef to_"], "retries_attempted": 1}