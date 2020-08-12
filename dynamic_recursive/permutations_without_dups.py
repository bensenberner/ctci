def perms_without_dups(string):
    n = len(string)

    def __perm(start_idx, exclusive_end_idx):
        if start_idx + 1 == exclusive_end_idx:
            return [[string[start_idx]]]
        results = []
        for idx in range(start_idx, exclusive_end_idx):
            suffices = __perm()

    def _perm(l):
        if len(l) <= 1:
            return [l]
        results = []
        for idx, element in enumerate(l):
            suffixes = _perm(l[:idx] + l[idx + 1 :])
            combos = [[element] + suffix for suffix in suffixes]
            results.extend(combos)
        return results

    return ["".join(permutation_list) for permutation_list in _perm(list(string))]
