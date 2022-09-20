{"text": "def kth(arr, k):\n    pivot = arr[0]\n    below = [x for x in arr if x < pivot]\n    above = [x for x in arr if x > pivot]\n\n    num_less = len(below)\n    num_lessoreq = len(arr) - len(above)\n\n    if k < num_less:\n        return kth(below, k)\n    elif k >= num_lessoreq:\n        pivot = arr[-1]\n        return kth(above, k)\n    else:\n        return pivot", "parts": ["def kth(arr, k):\n    pivot = arr[0]\n    below = [x for x in arr if x < pivot]\n    above = [x for x in arr if x > pivot]\n\n    num_less = len(below)\n    num_lessoreq = len(arr) - len(above)\n\n    if k < num_less:\n        return kth(below, k)\n    elif k >= num_lessoreq:\n        ", "\n    else:\n        return pivot"], "infills": ["pivot = arr[-1]\n        return kth(above, k)"], "retries_attempted": 1}