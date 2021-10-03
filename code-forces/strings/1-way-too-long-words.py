"""
https://codeforces.com/problemset/problem/71/A
800
"""
import unittest

test_cases = [
    ('word', 'word'),
    ('localization', 'l10n'),
    ('internationalization', 'i18n'),
    ('pneumonoultramicroscopicsilicovolcanoconiosis', 'p43s')
]


def shorten(word):
    word_len = len(word)
    if word_len > 10:
        return word[0] + str(word_len - 2) + word[-1]
    return word

class TestWayTooLongWords(unittest.TestCase):
    def test_shorten(self):
        for test_case in test_cases:
            res = shorten(test_case[0])
            assert res == test_case[1], f'{test_case}, {res}'

if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        res.append(shorten(input()))
    for result in res:
        print(result)