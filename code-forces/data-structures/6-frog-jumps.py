# https://codeforces.com/problemset/problem/1324/C


### https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/13/Slides13.pdf

"""
Tried testing out a binary search coupled with check_jump(). It failed on code forces
with with a long 'RRRRRRRRRR...' test case. Swapped it with a greedy search instead
"""


import unittest


def check_jump(d, jump_arr):
    start_position = -1
    while True:
        if start_position + d + 1 > len(jump_arr):
            return True

        found_right = False
        for i in range(start_position+1, start_position+d+1):
            j = jump_arr[i]
            if j == 'R':
                start_position = i
                found_right = True
                break

        if not found_right:
            return False


def search_possible_jumps(jump_arr):
    jumps = list(map(lambda j: len(j), jump_arr.split('R')))
    max_jump = max(jumps)+1
    if check_jump(max_jump, jump_arr):
        return max_jump


test_cases = [
    ('LRLRRLL', 3),
    ('L', 2),
    ('LLR', 3),
    ('RRRR', 1),
    ('LLLLLL', 7),
    ('R', 1)
]

class TestFrogJumps(unittest.TestCase):
    def test_cases(self):
        for test_case in test_cases:
            min_jumps = search_possible_jumps(test_case[0])
            assert min_jumps == test_case[1], f'{test_case[0]}, {test_case[1]}, out = {min_jumps}'


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        print(search_possible_jumps(input()))
