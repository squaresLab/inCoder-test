def powerset(arr):
    if arr:
        <insert>
        rest_subsets = powerset(rest)
        return [[first] + subset for subset in rest_subsets]
    else:
        return [[]]