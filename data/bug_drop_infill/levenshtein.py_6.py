{"text": "def levenshtein(source, target):\n    if source == '' or target == '':\n        return len(source) or len(target)\n\n    elif source[0] == target[0]:\n        source = source[1:]\n        target = target[1:]\n\n    else:\n        return 1 + min(\n            levenshtein(source,     target[1:]),\n            levenshtein(source[1:], target[1:]),\n            levenshtein(source[1:], target)\n        )", "parts": ["def levenshtein(source, target):\n    if source == '' or target == '':\n        return len(source) or len(target)\n\n    elif source[0] == target[0]:\n        ", "\n\n    else:\n        return 1 + min(\n            levenshtein(source,     target[1:]),\n            levenshtein(source[1:], target[1:]),\n            levenshtein(source[1:], target)\n        )"], "infills": ["source = source[1:]\n        target = target[1:]"], "retries_attempted": 1}