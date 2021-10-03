"""
https://codeforces.com/problemset/problem/115/A
"""
import unittest


test_cases = [
    ('5', ['-1', '1', '2', '1', '-1'], 3),
    ('4', ['-1', '1', '2', '3'], 4),
    ('12', ['-1', '1', '2', '3', '-1', '5', '6', '7', '-1', '9', '10', '11'], 4),
    ('6', ['-1', '-1', '2', '3', '1', '1'], 3),
    ('5', ['4', '5', '1', '-1', '4'], 3),
    ('1', ['-1'], 1),
    ('3', ['2', '-1'], 1),
    ('2', ['-1', '-1'], 1)
]

def party(n, parties):
    try:
        n = int(n)

        if len(parties) == 1:
            return 1
        elif len(set(parties)) == 1:
            return 1
        levels = 1
        for i in range(n):
            node = int(parties[i])
            current_levels = 0
            while node != -1:
                node = int(parties[node-1])
                current_levels += 1
                levels = max(levels, current_levels)
        return levels + 1
    except:
        return levels

class TestParty(unittest.TestCase):
    def test_party(self):
        for test_case in test_cases:
            n, parties, expected_out = test_case
            res = party(n, parties)
            assert res == expected_out, f'{test_case}, {res}'

if __name__ == '__main__':
    n = int(input())
    parties = []
    for _ in range(n):
        parties.append(input())

    print(party(n, parties))