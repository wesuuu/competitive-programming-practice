"""
https://codeforces.com/problemset/problem/112/A
800
"""
import unittest


test_cases = [
    (('aaaa', 'aaaA'), 0),
    (('abs', 'Abz'), -1),
    (('abcdefg', 'AbCdEfF'), 1)
]

def longer_string(s1, s2):
    for i in range(len(s1)):
        val1 = s1.lower()
        val2 = s2.lower()

        if val1 != val2 and val1 < val2:
            return -1
        elif val1 != val2 and val1 > val2:
            return 1
    return 0


class TestPetyaAndStrings(unittest.TestCase):
    def test_longer_strings(self):
        for test_case in test_cases:
            strings = test_case[0]
            res = longer_string(strings[0], strings[1])
            assert test_case[1] == res, f'{test_case}, {res}'

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(longer_string(s1, s2))