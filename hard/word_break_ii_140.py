from functools import lru_cache
from typing import List


def wordBreak(s: str, word_dict: List[str]) -> List[str]:
    word_dict = set(word_dict)
    if not s:
        return []

    @lru_cache(maxsize=None)
    def _recur(start_idx, end_idx):
        string = s[start_idx:end_idx]
        sub_result = set()
        if string in word_dict:
            sub_result.add(string)
        for partition_idx in range(start_idx + 1, end_idx):
            all_left_parts = _recur(start_idx, partition_idx)
            all_right_parts = _recur(partition_idx, end_idx)
            for left_part in all_left_parts:
                for right_part in all_right_parts:
                    sub_result.add(left_part + " " + right_part)
        return sub_result

    result = _recur(0, len(s))
    print(_recur.cache_info())
    return result
