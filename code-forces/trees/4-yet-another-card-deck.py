"""
1100
https://codeforces.com/problemset/problem/1511/C
"""

import unittest

test_cases = [
    (('7 5', '2 1 1 4 3 3 1', '3 2 1 1 4'), '5 2 3 1 5'),
]

def solve(nq, a, t):
    n, q = map(int, nq.split(' '))
    a = list(map(int, a.split(' ')))
    t = list(map(int, t.split(' ')))

    out = []
    for color in t:  # O(T)
        i = a.index(color)  # O(N)
        out.append(str(i + 1))
        a[:i+1] = [color] + a[:i] # shift the list #O(1)
    return ' '.join(out)

class TestYetAnotherCardDeck(unittest.TestCase):
    def test_solve(self):
        for test_case in test_cases:
            i = test_case[0]
            res = solve(i[0], i[1], i[2])
            assert res == test_case[1], f'{test_case}, {res}'

if __name__ == '__main__':
    nq = input()
    a = input()
    t = input()
    
    print(solve(nq, a, t))