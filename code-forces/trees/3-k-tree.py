"""
1600
https://codeforces.com/problemset/problem/431/C
"""
import unittest


test_cases = [
    ('3 3 2', '3'),
    ('3 3 3', '1'),
    ('4 3 2', '6'),
    ('4 5 2', '7'),
    ('70 6 1', '592826579')
]

import collections

def solve(nkd):
    n, k, d = map(int, nkd.split(' '))
    # calculate the full sum tree - sub sum tree that is < d
    return int((ktree(n, k) - ktree(n, d-1)) % (10 ** 9 + 7))

def ktree(n, k):
    m = collections.defaultdict(lambda: 0)
    m[0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            # calculate all the ways you can arrive at n = i using k numbers
            diff = i - j
            # negative numbers will not be placed into the hashmap
            if diff in m:
                m[i] += m[diff]
    return m[n]

class TestKtree(unittest.TestCase):
    def test_ktree(self):
        for test_case in test_cases:
            res = solve(test_case[0])
            assert res == int(test_case[1]), f'{test_case}, {res}'

if __name__ == '__main__':
    nkd = input()

    print(solve(nkd))