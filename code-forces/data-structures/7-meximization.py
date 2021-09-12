"""
https://codeforces.com/problemset/problem/1497/A

MEX is the lowest non-negative integer that is not in the set
MEX({1,2,3}) = 0; # 0 is not in the set and is the lowest non-negative integer

"""

import unittest

# input, output
test_cases = [
    ('4 2 0 1 3 3 7', '0 1 2 3 4 7 3'),
    ('2 2 8 6 9', '2 6 8 9 2'),
    ('0', '0')
]

def meximize(i):  #O(N) + O(N Log N) + O(N) = O(N log N)
    t = list(map(lambda el: int(el), i.split(' '))) # O(N)
    t.sort() # O(N Log N)

    meximized = []
    extras = []
    prev = -1
    for el in t: # O(N)
        if el == prev:
            extras.append(str(el))
        else:
            meximized.append(str(el))
        prev = el

    return " ".join(meximized + extras)


class TestMeximize(unittest.TestCase):

    def test_cases(self):
        for test_case in test_cases:
            i = test_case[0]
            ans = meximize(i)
            assert meximize(i) == test_case[1], f'{i}, {test_case[1]}'

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        l = input()
        test_case = input()
        print(meximize(test_case))
