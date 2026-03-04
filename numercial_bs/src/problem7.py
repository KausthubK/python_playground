"""
Problem 7: String & Array Manipulation
========================================
~10 minutes | Pure Python (no external imports)

Part A: Group Anagrams
Given a list of strings, group the anagrams together. Two strings are anagrams
if they contain the same characters with the same frequencies.

    group_anagrams(words: list[str]) -> list[list[str]]
    - Returns groups of anagrams (each group is a list of strings)
    - Within each group, strings should be in the order they appeared in the input
    - The groups themselves should be ordered by the index of their first element
      in the input (i.e., the group containing words[0] comes first)
    - Empty input returns []

    Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Part B: Can Form Palindrome
Given a string, determine if any permutation of it could form a palindrome.

    can_form_palindrome(s: str) -> bool
    - A palindrome reads the same forwards and backwards
    - For even-length strings: every character must appear an even number of times
    - For odd-length strings: at most one character can appear an odd number of times
    - Empty string is a palindrome

    Examples:
        can_form_palindrome("civic") -> True   (already a palindrome)
        can_form_palindrome("aab") -> True      (can form "aba")
        can_form_palindrome("abc") -> False     (no palindrome possible)

Constraint: No external imports. Use only built-in Python.
"""

from collections import Counter
import pandas as pd

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = []
    if words:
        counters = [Counter(i) for i in words]
        df = pd.DataFrame(counters, index=words).fillna(0).astype(int)
        groups = df.groupby(list(df.columns), sort=False).apply(lambda g: g.index.tolist()).tolist()
    return groups

def _is_odd(i: int) -> bool:
    return bool(i % 2)

def can_form_palindrome(s: str) -> bool:
    if len(s) == 0:
        return True # trivial case
    c = Counter(s)
    odd_count_chars = [k for k, v in dict(c).items() if _is_odd(v)]
    if _is_odd(i=len(s)):
        if len(odd_count_chars) == 1:
            return True
        return False
    else:
        if len(odd_count_chars) == 0:
            return True
        return False