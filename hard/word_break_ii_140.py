from functools import lru_cache
from typing import List


def wordBreak(s: str, word_dict: List[str]) -> List[str]:
    word_set = set(word_dict)

    @lru_cache(maxsize=len(s))
    def dfs(start_idx):
        result = []
        if start_idx == len(s):
            return result
        if s[start_idx:] in word_set:
            result.append(s[start_idx:])
        for word in word_set:
            if s[start_idx:].startswith(word):
                suffixes = dfs(start_idx + len(word))
                result.extend([f"{word} {suffix}" for suffix in suffixes])
        return result

    return dfs(0)
