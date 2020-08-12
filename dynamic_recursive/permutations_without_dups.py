def perms_without_dups(string):
    n = len(string)

    def _perm(l):
        if len(l) <= 1:
            return [l]
        results = []
        for idx, element in enumerate(l):
            suffixes = _perm(l[0:idx] + l[idx + 1 : n])
            combos = [[element] + suffix for suffix in suffixes]
            results.extend(combos)
        return results

    return ["".join(permutation_list) for permutation_list in _perm(list(string))]
