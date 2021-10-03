"""
https://codeforces.com/problemset/problem/1542/B
1500
"""
import unittest

test_cases = [
    (('24', '3', '5'), 'Yes'),
    #(('10', '3', '6'), 'No'),
    #(('2345', '1', '4'), 'Yes'),
    #(('19260817', '394', '485'), 'No'),
    #(('19260817', '233', '264'), 'Yes'),
    #(('631804787', '1', '21'), 'No')
]


def in_set(n, a, b):
    """Create the set by continuously updating values 
    
    if a == 1, will get stuck in a loop, return No
    """
    n = int(n)
    a = int(a)
    b = int(b)

    r = 1

    while r <= n:
        if (n - r) % b == 0:
            return 'Yes'
        r *= a
        if a == 1:
            return 'No'

    return 'No'

class TestPlusAndMultiply(unittest.TestCase):
    def test_in_set(self):
        for test_case in test_cases:
            n, a, b = test_case[0]
            got = in_set(n, a, b)
            assert got == test_case[1], f'{test_case}, {got}'

if __name__ == '__main__':
    for _ in range(int(input())):
        n, a, b = tuple(map(int, input().split(' ')))
        print(in_set(n, a, b))