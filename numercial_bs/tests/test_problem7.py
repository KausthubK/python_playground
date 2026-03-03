import pytest
from src.problem7 import group_anagrams, can_form_palindrome


class TestGroupAnagrams:
    def test_classic_example(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    def test_empty_input(self):
        assert group_anagrams([]) == []

    def test_no_anagrams(self):
        result = group_anagrams(["abc", "def", "ghi"])
        assert result == [["abc"], ["def"], ["ghi"]]

    def test_all_anagrams(self):
        result = group_anagrams(["abc", "bca", "cab"])
        assert result == [["abc", "bca", "cab"]]

    def test_single_word(self):
        assert group_anagrams(["hello"]) == [["hello"]]

    def test_empty_strings(self):
        result = group_anagrams(["", "", "a"])
        assert result == [["", ""], ["a"]]

    def test_preserves_input_order_within_groups(self):
        result = group_anagrams(["bca", "abc", "cab"])
        # "bca" appeared first, so it should be first in its group
        assert result == [["bca", "abc", "cab"]]

    def test_group_order_by_first_appearance(self):
        result = group_anagrams(["dog", "cat", "god", "tac"])
        # "dog" group first (index 0), "cat" group second (index 1)
        assert result == [["dog", "god"], ["cat", "tac"]]

    def test_mixed_case_not_anagram(self):
        """'Eat' and 'eat' are NOT anagrams (case-sensitive)."""
        result = group_anagrams(["Eat", "eat"])
        assert result == [["Eat"], ["eat"]]


class TestCanFormPalindrome:
    def test_already_palindrome(self):
        assert can_form_palindrome("civic") == True
        assert can_form_palindrome("racecar") == True

    def test_rearrangeable(self):
        assert can_form_palindrome("aab") == True    # -> "aba"
        assert can_form_palindrome("aabb") == True   # -> "abba"

    def test_not_possible(self):
        assert can_form_palindrome("abc") == False
        assert can_form_palindrome("abcd") == False

    def test_empty_string(self):
        assert can_form_palindrome("") == True

    def test_single_char(self):
        assert can_form_palindrome("x") == True

    def test_all_same(self):
        assert can_form_palindrome("aaaa") == True
        assert can_form_palindrome("aaa") == True

    def test_two_different(self):
        assert can_form_palindrome("ab") == False

    def test_long_string(self):
        # "aabbccdd" -> can form "abcddcba"
        assert can_form_palindrome("aabbccdd") == True
        # "aabbccde" -> 'd' and 'e' both odd -> False
        assert can_form_palindrome("aabbccde") == False
