"""
https://codeforces.com/problemset/problem/339/A
800
"""
import unittest


test_cases = [
    ('3+2+1', '1+2+3'),
    ('1+1+3+1+3', '1+1+1+3+3'),
    ('2', '2')
]

def order(s):
    nums = list(map(int, s.split('+')))
    nums.sort()
    ans = ''
    for num in nums:
        ans = ans + str(num) + '+'

        if num > 3:
            break

    return ans[:-1]


class TestHelpfulMaths(unittest.TestCase):
    def test_order(self):
        for test_case in test_cases:
            ans = order(test_case[0])
            assert ans == test_case[1], f'{test_case}, {ans}'

if __name__ == '__main__':
    print(order(input()))