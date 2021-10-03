"""
1700
https://codeforces.com/problemset/problem/339/D

TODO continue later
"""
import unittest
# x | y = or
# x ^ y = xor
test_cases = [
    (('2 4', '1 6 3 5', ['1 4', '3 4', '1 2', '1 2']), ['1', '3', '3', '3']),
    (('1 1', '1 1', ['1 1']), ['1']),
    (('1 10', '6 26', ['1 11', '1 9', '1 31', '1 10', '2 12', '1 8', '2 10', '2 4', '2 18', '1 31']), ['27', '27', '31', '26', '14', '12', '10', '12', '26', '31'])
]

# n = array length?
# m = num_queries

from functools import reduce

def solve(n, m, seq, query):
    p, b = query
    seq[p-1] = b
    first = []
    second = []
    first = [seq[i] | seq[i+1] for i in range(0, 2 ** n, 2)]
    for i in range(0, len(first), 2):
        second.append(reduce(lambda x, y: x ^ y, first[i:i+2]))

    return seq, second[0]

class TestXeniaAndBitOperations(unittest.TestCase):
    def test_solve(self):
        for test_case in test_cases:
            t = test_case[0]
            n, m = list(map(int, t[0].split(' ')))
            seq = list(map(int, t[1].split(' ')))
            for q, ans in zip(t[2], test_case[1]):
                q = tuple(map(int, q.split(' ')))
                seq, res = solve(n, m, seq, q)
                assert res == int(ans), f'{t}, {q}, out = {res}, ans = {ans}'

if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    seq = list(map(int, input().split(' ')))
    for _ in range(m):
        q = tuple(map(int, input().split(' ')))
        seq, ans = solve(n, m, seq, q)
        print(ans)