def levenshtein(source, target):
    if source == '' or target == '':
        return len(source) or len(target)

    <insert>
        return 1 + levenshtein(source[1:], target[1:])

    else:
        return 1 + min(
            levenshtein(source,     target[1:]),
            levenshtein(source[1:], target[1:]),
            levenshtein(source[1:], target)
        )