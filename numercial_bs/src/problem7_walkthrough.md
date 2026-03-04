# Problem 7 Walkthrough: String & Array Manipulation

## Part A: Group Anagrams

### Key Insight: anagrams have the same sorted characters

"eat", "tea", and "ate" all sort to `('a', 'e', 't')`. Use this as a dictionary key to group words.

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
```

### Walk through the example

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`

| Word | `sorted()` | Key | Dict state |
|------|-----------|-----|------------|
| "eat" | ['a','e','t'] | ('a','e','t') | {('a','e','t'): ["eat"]} |
| "tea" | ['a','e','t'] | ('a','e','t') | {('a','e','t'): ["eat","tea"]} |
| "tan" | ['a','n','t'] | ('a','n','t') | {... ('a','n','t'): ["tan"]} |
| "ate" | ['a','e','t'] | ('a','e','t') | {('a','e','t'): ["eat","tea","ate"], ...} |
| "nat" | ['a','n','t'] | ('a','n','t') | {... ('a','n','t'): ["tan","nat"]} |
| "bat" | ['a','b','t'] | ('a','b','t') | {... ('a','b','t'): ["bat"]} |

Result: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`

### Why does ordering work?

- **Within groups**: we iterate the input in order and `append`, so words appear in input order.
- **Group order**: Python dicts (3.7+) preserve insertion order, so the first group encountered (containing `words[0]`) comes first.

### Why `tuple(sorted(word))` and not `Counter`?

- `Counter` is not hashable — can't be a dict key
- Sorted tuple is hashable, simple, and O(k log k) where k is word length
- For very long words with small alphabets, a character-count tuple would be O(k): `tuple(word.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')` — but sorted is simpler and k is usually small

### Why `setdefault` over `defaultdict`?

Either works. `setdefault` avoids an import and does the same thing:

```python
# These are equivalent:
groups.setdefault(key, []).append(word)

# vs
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(word)
```

### Complexity

- **Time**: O(n * k log k) — n words, each sorted in O(k log k)
- **Space**: O(n * k) — storing all words in the dict

### Your original approach: pandas DataFrame

```python
counters = [Counter(i) for i in words]
df = pd.DataFrame(counters, index=words).fillna(0).astype(int)
groups = df.groupby(list(df.columns), sort=False).apply(lambda g: g.index.tolist()).tolist()
```

This is a creative approach — each word becomes a row of character frequencies, and groupby finds matching rows. Problems:
- **Violates the constraint** (no external imports)
- **Breaks with duplicate words** — pandas index must be unique, so `["eat", "eat"]` would fail
- **Performance** — pandas overhead is massive for this (~20x slower in the tests)

---

## Part B: Can Form Palindrome

### Key Insight: at most one character can have an odd count

A palindrome is symmetric — characters pair up from both ends. For even-length strings every character needs a partner (all even counts). For odd-length strings one character can sit in the middle (one odd count allowed). The rule `odd_count <= 1` covers both cases.

```python
def can_form_palindrome(s: str) -> bool:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    odd_count = sum(1 for v in counts.values() if v % 2)
    return odd_count <= 1
```

### Walk through examples

**"aab"** → counts: `{'a': 2, 'b': 1}` → odd count: 1 → `True` (can form "aba")

**"abc"** → counts: `{'a': 1, 'b': 1, 'c': 1}` → odd count: 3 → `False`

**""** → counts: `{}` → odd count: 0 → `True`

### Why you don't need separate even/odd length checks

Your original code checked string length parity separately:

```python
if _is_odd(len(s)):
    if len(odd_count_chars) == 1: return True
    return False
else:
    if len(odd_count_chars) == 0: return True
    return False
```

This is correct but unnecessary. If the string length is even, it's mathematically impossible to have exactly 1 odd-count character (the total count of characters is even, so the number of odd-count characters must be even too — it's 0 or 2+). So `<= 1` naturally gives 0 for even-length and 0-or-1 for odd-length.

### Complexity

- **Time**: O(n) — single pass to count, single pass over counts
- **Space**: O(k) — where k is the number of distinct characters (at most 26 for lowercase)

---

## Interview Q&A

### Q1: Can you solve group_anagrams without sorting?

Yes — use a character frequency tuple as the key:

```python
key = tuple(word.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')
```

This is O(n * 26) = O(n) per word instead of O(n * k log k). Worth it only when words are very long.

### Q2: What if the input has duplicate words like `["eat", "eat"]`?

The sorted-tuple approach handles this correctly — both map to the same key and end up in the same group: `[["eat", "eat"]]`. The pandas approach would break because it uses words as the DataFrame index.

### Q3: How would you handle case-insensitive anagram grouping?

Normalize before keying: `key = tuple(sorted(word.lower()))`. Keep the original word in the group.

### Q4: For `can_form_palindrome`, could you do it without counting all characters?

Yes — use a set. Toggle characters in/out: if a character is in the set, remove it; otherwise add it. At the end, the set contains characters with odd counts.

```python
def can_form_palindrome(s: str) -> bool:
    odd_chars = set()
    for ch in s:
        odd_chars.symmetric_difference_update(ch)
    return len(odd_chars) <= 1
```

Same complexity but avoids storing counts — just tracks parity.