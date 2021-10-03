"""
https://codeforces.com/problemset/problem/1409/D
1500
"""
import unittest


test_cases = [
    ('2 1', '8'),
    ('1 1', '0'),
    ('500 4', '500'),
    ('217871987498122 10', '2128012501878'),
    ('100000000000000001 1', '899999999999999999'),
    ('267367244641009859 50', '58990141'),
    ('621306592075475634 48', '524366')
]

def get_sum(ns):
    """
    set divisor = 10
    Increase n to the number % divisor == 0
    Calculate the sum of digits, if not <= s, increase divisor by another digit = 0
    """
    n, s = ns.split(' ')
    s = int(s)
    num_digits = len(n)
    digits = [int(char) for char in n]
    sum_digits = sum(digits)
    if sum_digits <= s:
        return '0'

    n_copy = int(n)
    start = 1
    while True:
        start *= 10
        n_copy = n_copy + start - (n_copy % start)
        digits = [int(char) for char in str(n_copy)]
        if sum(digits) <= s:
            return str(int(''.join(map(str, digits))) - int(n))



class TestDecreaseTheSumOfDigits(unittest.TestCase):
    def test_get_sum(self):
        for test_case in test_cases:
            got = get_sum(test_case[0])
            assert got == test_case[1], f'{test_case}, {got}'

if __name__ == '__main__':
    for _ in range(int(input())):
        ns = input()
        print(get_sum(ns))