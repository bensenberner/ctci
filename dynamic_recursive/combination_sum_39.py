from typing import List


class Cache:
    def __init__(self):
        self.c = dict()

    def get(self, candidates_list, target):
        return self.c.get(tuple(candidates_list), target)

    def add(self, candidates_list, target, result):
        self.c[(tuple(candidates_list), target)] = result


def combinationSumOriginal(candidates: List[int], target: int) -> List[List[int]]:
    ways_to_sum_to = [set() for _ in range(target + 1)]
    for num in range(1, target + 1):
        if num in candidates:
            ways_to_sum_to[num] = {(num,)}
        for candidate in candidates:
            if num - candidate < 0:
                continue
            extension = {
                tuple(sorted(list(way) + [candidate]))
                for way in ways_to_sum_to[num - candidate]
            }
            ways_to_sum_to[num] = ways_to_sum_to[num].union(extension)
    return [list(way) for way in ways_to_sum_to[target]]


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    curr_attempt = []
    num_cands = len(candidates)

    def _backtrack(start_idx, curr_sum):
        if curr_sum > target:
            return
        if curr_sum == target:
            result.append(curr_attempt[:])
            return
        for cand_idx in range(start_idx, num_cands):
            candidate = candidates[cand_idx]
            curr_attempt.append(candidate)
            _backtrack(cand_idx, candidate + curr_sum)
            curr_attempt.pop()

    _backtrack(0, 0)
    return result
