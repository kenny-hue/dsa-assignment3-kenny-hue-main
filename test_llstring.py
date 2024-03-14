import unittest
from llstring import LLString

class TestLLString(unittest.TestCase):
    def setUp(self):
        self.llstring = LLString('hello')

    def test_find(self):
        assert self.llstring.find('l') == 2

    def test_find_does_not_exist(self):
        assert self.llstring.find('x') == -1

    def test_to_upper_case(self):
        self.llstring.to_upper_case()
        assert self.llstring.to_string() == 'HELLO'

    def test_to_upper_case_empty(self):
        empty_list = LLString('')
        empty_list.to_upper_case()
        assert empty_list.to_string() == ''

    def test_replace(self):
        self.llstring.replace('l', 'z')
        assert self.llstring.to_string() == 'hezzo'

    def test_replace_does_not_exist(self):
        self.llstring.replace('x', 'z')
        assert self.llstring.to_string() == 'hello'

    def test_copy(self):
        new_llstring = self.llstring.copy()
        assert new_llstring != self.llstring
        assert new_llstring.to_string() == self.llstring.to_string()

    def test_trim(self):
        trim_str = LLString(' hello')
        trim_str.trim()
        assert trim_str.to_string() == 'hello'

    def test_trim_nospace(self):
        self.llstring.trim()
        assert self.llstring.to_string() == 'hello'

    def test_find_nth(self):
        assert self.llstring.find_nth(2, 'l') == 3

    def test_find_nth_does_not_exist(self):
        assert self.llstring.find_nth(2, 'e') == -1
