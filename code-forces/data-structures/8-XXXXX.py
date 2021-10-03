"""
1200
https://codeforces.com/problemset/problem/1364/A
"""
import unittest

# array, divides, expected_output
test_cases = [
    ('1 2 3', '3', '2'),
    ('1 2 3', '4', '3'),
    ('0 6', '2', '-1'),
    ('9', '3', '-1'),
    ('7', '4', '1'),
    ('0', '1', '-1'),
    ('10000 5000 5000 10000 0', '10000', '3'),
    ('0 1 0 1 0 1 0 1', '2', '7')
]


def longest_subarray(arr_str, x, n):
    """Calc the sum of the array. Return n if mod(sum, x) != 0
    
    In the other cases:
    - Iterate over the length of the array
      - Select the current index from start (i) and last index (-i - 1)
      - Determine if the sum - selected number at index i, -i-1 still divides. If it doesn't
        return the length subtracted from that distance
    """
    x = int(x)
    n = int(n)
    arr = list(map(lambda i: int(i), arr_str.split(' ')))  #O(N)
    arr_sum = sum(arr)

    if arr_sum % x != 0:
        return n
    else:
        for i in range(n):  # At most O(N)
            start = arr_sum - arr[i]
            end = arr_sum - arr[-i-1]
            if start % x != 0:
                return n - i - 1
            elif end % x != 0:
                return n - i - 1
    return -1


class TestXXXXX(unittest.TestCase):
    def test_cases(self):
        for test_case in test_cases:
            res = longest_subarray(test_case[0], test_case[1], len(test_case[0].split(' ')))
            assert str(res) == test_case[2], f'{test_case}, out = {res} != {test_case[2]}'


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        nx = input()
        nx = nx.split(' ')
        n, x = nx[0], nx[1]
        arr = input()
        print(longest_subarray(arr, x, n))