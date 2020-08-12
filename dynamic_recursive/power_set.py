from typing import Set


def power_set(original_set):
    memo = dict()

    def _power_set(s: Set) -> Set:
        s_tuple = tuple(s)
        if s_tuple in memo:
            return memo[s_tuple]
        ps = set()
        # go through each sub element, add them in, then add the full thing
        for element in s:
            reduced_set = s.difference({element})
            reduced_power_set = _power_set(reduced_set)
            ps.update(reduced_power_set)
        ps.add(s_tuple)
        memo[s_tuple] = ps
        return ps

    return [set(e) for e in _power_set(original_set)]
