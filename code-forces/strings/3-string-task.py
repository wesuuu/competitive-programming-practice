"""
https://codeforces.com/problemset/problem/118/A
1000
"""
import unittest


test_cases = [
    ('tour', '.t.r'),
    ('Codeforces', '.c.d.f.r.c.s'),
    ('aBAcAba', '.b.c.b'),
    ('xnhcigytnqcmy', '.x.n.h.c.g.t.n.q.c.m')
]

def string_task(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    modified_string = []
    for char in string:
        char = char.lower()
        if char not in vowels:
            modified_string.append(f'.{char}')

    return ''.join(modified_string)


class TestStringTask(unittest.TestCase):
    def test_string_task(self):
        for test_case in test_cases:
            ans = string_task(test_case[0])
            assert ans == test_case[1], f'{test_case}, {ans}'

if __name__ == '__main__':
    print(string_task(input()))